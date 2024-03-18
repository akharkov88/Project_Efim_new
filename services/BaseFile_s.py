import traceback

from typing import (
    List,
    Optional,
)

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

import models
import tables
import os
import pandas as pd
import pathlib
from services.auth import  get_session
from fastapi.encoders import jsonable_encoder
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.cell import Cell, MergedCell
from openpyxl.styles import PatternFill
from openpyxl.utils.cell import get_column_letter
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Alignment
# from database import get_current_user
#
# print(get_current_user)
class BaseFileServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    def unload_file(self,file,
                    user: tables.User,
                    ) -> str:
        filename=self.create_uuid_table(file.filename,user)
        with open(pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())),"src","file",filename), "wb") as f:
            f.write(file.file.read())

        ff = '<table class="first iksweb" id="first_table">                        <tbody id="earthWorks_1">                        <tr style="background-color: #fce1b3">                            <td rowspan="2" class="tehstolbec">Тех столбец</td>                            <td>№</td>                            <td rowspan="2" style="font-weight: bold;">Наименование</td>                            <td colspan="4" style="font-weight: bold;">Стоимость</td>                            <td colspan="4" style="font-weight: bold;">Справочная информация</td>                            <td colspan="8" style="display:none" class="pto">Аналитический блок</td>                        </tr>                        <tr style="background-color: #fce1b3">                            <td style="font-weight: bold;">п/п</td>                            <td style="font-weight: bold;">Ед.изм.</td>                            <td style="font-weight: bold;">Кол-во</td>                            <td style="font-weight: bold;">Цена</td>                            <td style="font-weight: bold;">Всего</td>                            <td rowspan="1" style="font-weight: bold;">Тр-затр (чел-дн)</td>                            <td rowspan="1" style="font-weight: bold;">Столбец для анализа</td>                            <td rowspan="1" style="font-weight: bold;"></td>                            <td rowspan="1" style="font-weight: bold;">Примечание</td>                            <td style="display:none" class="pto">Кол-во</td>                            <td style="display:none" class="pto">Цена руб-ед</td>                            <td style="display:none" class="pto">Всего</td>                            <td style="display:none" class="pto">Тр-затр (чел-дн)</td>                            <td style="display:none" class="pto">Стоимость дня рабочего</td>                        </tr>                        </tbody>                        <tbody id="earthWorks_costWork_1">                        <tr>                            <td style="border-right: none;"></td>                            <td contenteditable="false" style="border-left: none; border-right: none;"></td>                            <td contenteditable="false" id="earthWorks_costWork_addLine_1" style="font-weight: bold; border-left: none;" colspan="4" onmouseover="showButton(event, this)" onmouseout="closeButton(event,this)">                            Стоимость работ                            <div style="display: none;"><button type="button" onclick="addLine(event,this)">addLine</button></div>                            </td>                            <td contenteditable="false"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                        </tr>                    </tbody><tbody id="earthWorks_costMaterial_1">                        <tr>                        <td style="border-right: none;"></td>                            <td contenteditable="false" style="border-left: none; border-right: none;"></td>                            <td contenteditable="false" id="earthWorks_costMaterial_addLine_1" style="font-weight: bold; border-left: none;" colspan="4" onmouseover="showButton(event, this)" onmouseout="closeButton(event,this)">                            Стоимость материала                            <div style="display: none;"><button onclick="addLine(event,this)">addLine</button></div>                            </td>                            <td contenteditable="false"></td>                            <td contenteditable="false" colspan="2" style="font-weight: bold;"> Ед изм расчётные </td>                            <td contenteditable="false" style="font-weight: bold;"> Ед изм (М2) для окраски </td>                            <td contenteditable="true"></td>                            <td contenteditable="false" style="display:none" class="pto">Закупка по счету - ед изм расчётные</td>                            <td contenteditable="false" style="display:none" class="pto">Остаток закупки</td>                            <td contenteditable="false" style="display:none" class="pto">ед изм к закупке</td>                            <td contenteditable="false" style="display:none" class="pto">руб-ед</td>                            <td contenteditable="false" style="display:none" class="pto"></td>                            <td contenteditable="false" style="display:none" class="pto">Счёта</td>                            <td contenteditable="false" style="display:none" class="pto">Срок поставки</td>                            <td contenteditable="false" style="display:none" class="pto">ПРИМЕЧАНИЕ</td>                        </tr>                    </tbody>                    <tbody id="earthWorks_Special_1">                    <tr>                    <td style="border-right: none;"></td>                            <td contenteditable="false" style="border-left: none; border-right: none;"></td>                             <td contenteditable="false" id="earthWorks_Special_addLine_1" style="font-weight: bold; border-left: none;" colspan="4" onmouseover="showButton(event, this)" onmouseout="closeButton(event,this)">                            Стоимость спецтехники                            <div style="display: none;"><button onclick="addLine(event,this)">addLine</button></div>                            </td>                            <td contenteditable="false"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="false" style="display:none" class="pto">Стоимость аренды</td>                            <td contenteditable="false" style="display:none" class="pto">Телефон</td>                            <td contenteditable="false" style="display:none" class="pto">Счет</td>                            <td contenteditable="false" style="display:none" class="pto">Срок</td>                        </tr>                    </tbody>                     <tbody id="earthWorks_Total_1">                        <tr>                        <td style="border-right: none;"></td>                            <td contenteditable="false" style="border-left: none; border-right: none;"></td>                            <td contenteditable="false" style="font-weight: bold;border-left: none;" colspan="4"> Итого                            </td>                            <td contenteditable="false"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                            <td contenteditable="true" style="display:none" class="pto"></td>                        </tr>                        <tr id="stroka">                        <td class="tehstolbec"></td>                            <td contenteditable="false">1</td>                            <td contenteditable="false" style="font-weight: bold;">                                Накладные расходы                            </td>                            <td contenteditable="false">%</td>                            <td contenteditable="true" class="percent"></td>                            <td contenteditable="true"></td>                            <td contenteditable="false"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                        </tr>                        <tr id="stroka">                        <td class="tehstolbec"></td>                            <td contenteditable="false">2</td>                            <td contenteditable="false" style="font-weight: bold;">                                Вспомогательные материалы                            </td>                            <td contenteditable="false">%</td>                            <td contenteditable="true" class="percent"></td>                            <td contenteditable="true"></td>                            <td contenteditable="false"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto" <="" td="">                            </td><td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                        </tr>                        <tr id="stroka">                        <td class="tehstolbec"></td>                            <td contenteditable="false">3</td>                            <td contenteditable="false" style="font-weight: bold;">                                Транспортные расходы                            </td>                            <td contenteditable="false">%</td>                            <td contenteditable="true" class="percent"></td>                            <td contenteditable="true"></td>                            <td contenteditable="false"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                            <td contenteditable="true" style="display:none" class="costWork_role_boss pto"></td>                        </tr>                        <tr id="stroka">                        <td class="tehstolbec"></td>                            <td contenteditable="false">4</td>                            <td contenteditable="false" style="font-weight: bold; text-align: right">                                ВСЕГО:                            </td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                        </tr>                        <tr id="stroka">                        <td class="tehstolbec"></td>                            <td contenteditable="false">5</td>                            <td contenteditable="false" style="font-weight: bold;">                                В том числе НДС - 20% за нал от материалов                            </td>                            <td contenteditable="false">%</td>                            <td contenteditable="true" class="percent"></td>                            <td contenteditable="true"></td>                            <td contenteditable="false"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                            <td contenteditable="true"></td>                        </tr>                    </tbody>                    <tbody id="result_total">                    <tr class="blank_row">                        <td colspan=""></td>                    </tr>                        <tr>                        <td class="tehstolbec"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false" style="font-weight: bold; text-align: right">                                ВСЕГО:                            </td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                        </tr>                        <tr>                        <td class="tehstolbec"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false" style="font-weight: bold;">                                В том числе НДС - 20% за нал от материалов                            </td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                            <td contenteditable="false"></td>                        </tr>                    </tbody>                    </table>'

        table = pd.read_html(ff)[0]
        # Store the dataframe in Excel file
        table.to_excel(pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())), "src", "file", filename))
        return filename

    def create_uuid_table(self, name_fail,user: tables.User,) -> tables.BaseFile:
            try:
                operation = tables.BaseFile(
                    name=name_fail,
                    user_name=user.username,

                )
                self.session.add(operation)
                self.session.commit()
                return str(operation.id)
            except:
                print(traceback.format_exc())
                raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Ошибка создания файла")
                # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})

            # return "operation"

    def get_name_file(self,id):
        try:
            operation = (
                self.session
                .query(tables.BaseFile)
                .filter(
                    tables.BaseFile.id == id
                )
                .first()
            )
            #посмотреть какой запрос получится
            print(operation.compile(compile_kwargs={"literal_binds":True}))

            if not operation:
                raise HTTPException(status.HTTP_404)
            # return jsonable_encoder(operation)
            return operation.name
        except:
            print(traceback.format_exc())
            raise HTTPException(status.HTTP_400_BAD_REQUEST)
            # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})


    def reports_PTO(self,table:str):
        import uuid
        uuid = str(uuid.uuid4())
        name_fail=uuid.replace("-","_")

        table = table.tables.replace('colspan="100%"', '')
        table = table.replace('\n                             ', '')
        table = table.replace('\n                    ', '')

        workbook = Workbook()
        sheet = workbook.active
        with_column = {}

        soup = BeautifulSoup(table, 'lxml')
        table = soup.find_all('table')[0]
        thin_border = Border(left=Side(style='thin'),
                             right=Side(style='thin'),
                             top=Side(style='thin'),
                             bottom=Side(style='thin'))

        try:
            row_marker = 1
            for row in table.find_all('tr'):
                column_marker = 1
                print(row)
                background_color = ""
                if row.get("style") and row.get("style").find("background-color") != -1:
                    background_color = row.get("style")[row.get("style").find("background-color: ") + 19:]
                columns = row.find_all('td')
                for column in columns:
                    if column.get("class")==None or "tehstolbec" not in column.get("class"):
                        print(column)

                        if column.datalist:
                            column.datalist.decompose()
                        text_value=""
                        if len(str(column.get_text()).replace(" ","").replace("\n",""))==0:
                            if column.div:
                                if column.div.input:
                                    text_value=column.div.input.get("value")
                            # else:
                            #     text_value=column.get_text()
                            ...
                        else:
                            if column.div:
                                column.div.decompose()
                            text_value=column.get_text()
                        print(column)

                        print("text_value", "&&"+text_value+"&&")
                        print("len text_value", len(text_value))
                        if len(text_value)==4:
                            pass


                        if row_marker == 4 and column_marker == 3:
                            ...
                        while isinstance(sheet.cell(row=row_marker, column=column_marker), MergedCell):
                            column_marker += 1
                        sheet.cell(row=row_marker, column=column_marker, value=text_value)
                        sheet.cell(row=row_marker, column=column_marker).border = thin_border
                        sheet.cell(row=row_marker, column=column_marker).alignment = Alignment(horizontal='center')
                        # print(with_column)
                        # print(get_column_letter(column_marker))
                        # print(text_value)
                        # print(len(text_value))
                        # if get_column_letter(column_marker)=="J":
                        #     pass
                        text_len = len(text_value)
                        if text_len != 0 and with_column.setdefault(get_column_letter(column_marker), text_len + 2):
                            if with_column[get_column_letter(column_marker)] <= text_len + 2:
                                with_column[get_column_letter(column_marker)] = text_len + 2
                                sheet.column_dimensions[get_column_letter(column_marker)].width = text_len + 2
                        if background_color != "":
                            sheet[row_marker][column_marker - 1].fill = PatternFill(start_color=background_color,
                                                                                    end_color=background_color,
                                                                                    fill_type="solid")

                        if column.get("colspan") or column.get("rowspan"):

                            merge_column = column_marker
                            merge_row = row_marker
                            if column.get("colspan"):
                                print(column.get("colspan"))
                                merge_column += int(column.get("colspan")) - 1
                            if column.get("rowspan"):
                                merge_row += int(column.get("rowspan")) - 1

                            sheet.merge_cells(start_row=row_marker, start_column=column_marker, end_row=int(merge_row),
                                              end_column=int(merge_column))
                        if column.get("colspan"):
                            column_marker += int(column.get("colspan")) - 1
                        # if column.get("rowspan"):
                        #     row_marker += int(column.get("rowspan"))-1

                        column_marker += 1
                row_marker += 1
            workbook.save(filename=pathlib.PurePath(pathlib.Path(os.path.abspath(os.getcwd())), "src", "file", name_fail))
        except:
            print(traceback.format_exc())
            workbook.save(filename="converter_html_in_xlsx.xlsx")
            print(traceback.format_exc())

        print(with_column)
        return name_fail
