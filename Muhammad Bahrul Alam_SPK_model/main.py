import sys

from colorama import Fore, Style
from models import Base, Laptop
from engine import engine

from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import MEREK_SCALE,SCALE_ram,SCALE_memori_internal,SCALE_processor,SCALE_layar,SCALE_baterai_mah,SCALE_harga_rp

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-7 (Kriteria)
        self.raw_weight = {
            'Merk': 5, 
            'ram': 3, 
            'memori_internal': 4, 
            'processor': 3, 
            'layar': 4, 
            'baterai_mah': 3, 
            'Harga' : 1
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Laptop)
        return [{
            'id': laptop.id,
            'Merk': MEREK_SCALE[laptop.Merk],
            'ram': SCALE_ram[laptop.ram],
            'memori_internal': SCALE_memori_internal[laptop.memori_internal],
            'processor': SCALE_processor[laptop.processor],
            'layar': SCALE_layar[laptop.layar],
            'baterai_mah': SCALE_baterai_mah[laptop.baterai_mah],
            'Harga': SCALE_harga_rp[laptop.Harga]
        } for laptop in session.scalars(query)]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]

        Merk = [] # max
        ram = [] # max
        memori_internal = [] # max
        processor = [] # max
        layar = [] # max
        baterai_mah = [] # max
        Harga = [] # min

        for data in self.data:
            Merk.append(data['Merk'])
            ram.append(data['ram'])
            memori_internal.append(data['memori_internal'])
            processor.append(data['processor'])
            layar.append(data['layar'])
            baterai_mah.append(data['baterai_mah'])
            Harga.append(data['Harga'])

        max_Merk = max(Merk)
        max_ram = max(ram)
        max_memori_internal = max(memori_internal)
        max_processor = max(processor)
        max_layar = max(layar)
        max_baterai_mah = max(baterai_mah)
        min_Harga = min(Harga)

        return [{
            'id': data['id'],
            'Merk': data['Merk']/max_Merk,
            'ram': data['ram']/max_ram,
            'memori_internal': data['memori_internal']/max_memori_internal,
            'processor': data['processor']/max_processor,
            'layar': data['layar']/max_layar,
            'baterai_mah': data['baterai_mah']/max_baterai_mah,
            'Harga': min_Harga/data['Harga']
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['id']:
            round(
                row['Merk'] ** weight['Merk'] *
                row['ram'] ** weight['ram'] *
                row['memori_internal'] ** weight['memori_internal'] *
                row['processor'] ** weight['processor'] *
                row['layar'] ** weight['layar'] *
                row['baterai_mah'] ** weight['baterai_mah'] *
                row['Harga'] ** (-weight['Harga'])
                , 2
            )

            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))

class SimpleAdditiveWeighting(BaseMethod):
    
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result =  {row['id']:
            round(
                row['Merk'] * weight['Merk'] +
                row['ram'] * weight['ram'] +
                row['memori_internal'] * weight['memori_internal'] +
                row['processor'] * weight['processor'] +
                row['layar'] * weight['layar'] +
                row['baterai_mah'] * weight['baterai_mah'] +
                row['Harga'] * weight['Harga']
                , 2
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
