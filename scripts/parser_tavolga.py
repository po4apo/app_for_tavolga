import pandas as pd
import math
import jsondata
from transliterate import translit
from generating import PasswordGenerator


class TavolgaParser:
    def __init__(self, xlsx_name) -> None:
        self.xlsx_pages = self.get_xlsx_pages_map(xlsx_name)
        self.nominations = list()
        self.pages = list()

    def get_xlsx_pages_map(self, xlsx_filepath: str):
        """
        TODO
        """
        xlsx = pd.ExcelFile(xlsx_filepath)

        df_map = dict()
        for sheet_name in xlsx.sheet_names:
            df_map[sheet_name] = xlsx.parse(sheet_name)        

        return df_map


    def prepare_main_data_by_nominations(self, left_col, right_col):
        """
        TODO
        """
        pages = list()
        i = 0
        for key in self.xlsx_pages:
            if not (i == 0 or i == len(self.xlsx_pages) - 1):
                pages.append(self.xlsx_pages[key].iloc[:, left_col:right_col])
            i += 1
        return pages


    def get_nomination_names(self, pages):
        """
        TODO
        """
        result = dict()
        for page in pages:
        # for i, row in page.iterrows():
        #     result.append(row[0])

            for column in page:
                result[column] = dict()
                break
        return result


    def prepare_by_fio(self, pages, part):
        #for page in pages:
        for page, nom in zip(pages, part):
            part[nom]['pandas_row'] = list()
            part[nom]['user_fio'] = list()
            for i, fio in enumerate(page.iloc[2:, 1]):
                if isinstance(fio, (float,)) and math.isnan(fio):
                    pass
                    #print(i, 'NaN')
                else:
                    part[nom]['pandas_row'].append(i + 2)
                    part[nom]['user_fio'].append(fio)
                    #print(i, ':', fio)
        return part


    def add_ratings(self, pages, part, stage, column):
        #for page in pages:
        for page, nom in zip(pages, part):
            part[nom][stage] = list()

            top_row = min(part[nom]['pandas_row'])
            bot_row = max(part[nom]['pandas_row'])
            for rating in page.iloc[top_row:bot_row, column]:
                if isinstance(rating, (float,)) and math.isnan(rating):
                    part[nom][stage].append(rating)
                    #print('NaN')
                else:
                    part[nom][stage].append(rating)
                    #print(rating)
        return part


    def generate_email(self, fio: str):
        fio = fio.strip()
        i = fio.rfind(' ')
        fio = fio[:i]
        trans_fio = translit(fio, 'ru', reversed=True)
        trans_fio = trans_fio.replace(' ', '', -1) 
        return trans_fio       


    def add_email(self, part):
        for nom in part:
            part[nom]['email'] = list()
            for fio in part[nom]['user_fio']:
                trans_fio = self.generate_email(fio)
                part[nom]['email'].append(f'{trans_fio}@tavolga.ru')
        return part


    def add_password(self, part):
        pgen = PasswordGenerator()
        for nom in part:
            part[nom]['password'] = list()
            for fio in part[nom]['user_fio']:
                passphrase = pgen.generate_passphrase()
                part[nom]['password'].append(passphrase)
        return part        


    @staticmethod    
    def save_as_binary_file(obj, path: str):
        """
        TODO
        """
        import pickle
        with open(path, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)    


if __name__ == '__main__':
    parser = TavolgaParser(xlsx_name := 'khakaton.xlsx')
    main_part_pages = parser.prepare_main_data_by_nominations(0, 5)
    main_part = parser.get_nomination_names(main_part_pages)
    main_part = parser.prepare_by_fio(main_part_pages, main_part)
    main_part = parser.add_ratings(main_part_pages, main_part, 'stage_1', 2)
    main_part = parser.add_ratings(main_part_pages, main_part, 'stage_2', 3)
    main_part = parser.add_ratings(main_part_pages, main_part, 'stage_3', 4)
    main_part = parser.add_email(main_part)
    main_part = parser.add_password(main_part)
    jsondata.save_to_json(main_part, 'tavolga.json')
    #parser.save_as_binary_file(parser.schedule, 'src.dump')
