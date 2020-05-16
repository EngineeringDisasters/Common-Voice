import torch
import torch.nn as nn
import torch.nn.functional as F

class AudioLSTM(nn.Module):
    """
    LSTM for audio classification
    """

    def __init__(
            self,
            input_size: int,
            hidden_size: int,
            dropout: float,
            num_layer: int,
            output_size: int,
            batch: bool = True,
            bidirectional: bool = True,
            RNN_TYPE: str = "LSTM",
    ) -> None:
        """
        :param input_size: The number of expected features in the input x
        :param hidden_size:The number of features in the hidden state h
        :param num_layer: Number of recurrent layers. E.g., setting num_layers=2 would mean stacking two LSTMs together
        to form a stacked LSTM, with the second LSTM taking in outputs of the first LSTM and computing the final results.
        :param dropout:f non-zero, introduces a Dropout layer on the outputs of each LSTM layer except the last layer,
        with dropout probability equal to dropout
        :param output_size: Number of label prediction
        :param batch If True, then the input and output tensors are provided as (batch, seq, feature)
        :param bidirectional: If True, becomes a bidirectional LSTM
        :param RNN_TYPE: Specify the type of RNN. Input takes two options LSTM and GRU
        """
        super(AudioLSTM, self).__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layer = num_layer
        self.dropout = dropout
        self.output_size = output_size

        if RNN_TYPE == "LSTM":
            self.RNN_TYPE = nn.LSTM(
                input_size=input_size,
                hidden_size=hidden_size,
                num_layers=num_layer,
                dropout=dropout,
                batch_first=batch,
                bidirectional=bidirectional,
            )

        if RNN_TYPE == "GRU":
            self.RNN_TYPE = nn.GRU(
                input_size=input_size,
                hidden_size=hidden_size,
                num_layers=num_layer,
                dropout=dropout,
                batch_first=batch,
                bidirectional=bidirectional,
            )

        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(hidden_size, output_size)
        self.out = nn.Sigmoid()

    def forward(self, x, hidden):
        """

        :param x:
        :param hidden: :
        :return:
        """

        seq_count = x.shape[1]
        x = x.float().view(1, -1, seq_count)
        lstm_out, hidden = self.RNN_TYPE(x, hidden)
        out = self.dropout(lstm_out)
        score = F.sigmoid(out)

        return score, hidden

    def init_hidden(self, batch_size: int):
        """
        Initializes hidden state. Create two new tensors with sizes n_layers x batch_size x hidden_dim, initialized to
        zero, for hidden state and cell state of LSTM.
        """

        weight = next(self.parameters()).data

        if torch.cuda.is_available():
            hidden = (
                weight.new(self.num_layer * self.output_size, batch_size, self.hidden_size).zero_().cuda(),
                weight.new(self.num_layer * self.output_size, batch_size, self.hidden_size).zero_().cuda(),
            )

        else:
            hidden = (
                weight.new(self.num_layer * self.output_size, batch_size, self.hidden_size).zero_(),
                weight.new(self.num_layer * self.output_size, batch_size, self.hidden_size).zero_(),
            )

        return hidden
