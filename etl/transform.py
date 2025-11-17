import os
import pandas as pd

#TODO:
# That should be modified for a Class. Transformer class with that transforming logic within seperated functions

class Transform:
    def __init__(self,df):
        self._df = df

    def _column_name(self): #for column

        if not isinstance(self._df,pd.DataFrame):
            self._df = pd.DataFrame(self._df)

        self._df.columns = ['open', 'high', 'low', 'close', 'volume']
        self._df = self._df.reset_index().rename(columns={'index': 'date'})
        self._df['date'] = pd.to_datetime(self._df['date'])
        self._df[['open', 'high', 'low', 'close']] = self._df[['open', 'high', 'low', 'close']].astype(float)
        self._df['volume'] = self._df['volume'].astype(int)


    def _add_new_column(self):
        self._df['daily_change_percentage'] = ((self._df['close'] - self._df['open']) / self._df['open']) * 100


    def _keep_in_folder(self,filename="output.csv"):

        if not isinstance(self._df,pd.DataFrame):
            self._df = pd.DataFrame(self._df)
        output_folder = "transformed/"

        os.makedirs(output_folder,exist_ok=True)

        output_path = os.path.join(output_folder,filename)

        self._df.to_csv(output_path,sep='\t',index=False,float_format='%.2f')

    def tranform_data(self):
        self._column_name()
        self._add_new_column()
        self._keep_in_folder()
