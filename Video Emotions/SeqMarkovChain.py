import pandas as pd
def SeqMarkovChain(seq):
    df = pd.DataFrame(seq)
    # create a new column with data shifted one space
    x = df['shift'] = df[0].shift(-1)
    # add a count column (for group by function)
    df['count'] = 1
    # groupby and then unstack, fill the zeros
    trans_mat = df.groupby([0, 'shift']).count().unstack().fillna(0)
    print(trans_mat)
    # normalise by occurences and save values to get transition matrix
    trans_mat = trans_mat.div(trans_mat.sum(axis=1), axis=0).values
    return trans_mat