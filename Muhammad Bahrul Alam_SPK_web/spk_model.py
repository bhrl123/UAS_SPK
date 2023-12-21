from settings import MEREK_SCALE,SCALE_ram,SCALE_memori_internal,SCALE_processor,SCALE_layar,SCALE_harga_rp,SCALE_baterai_mah

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

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

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]] # value int
                temp2 = {v: k for k, v in setWeight.items()}[item[1]] # key str

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': laptop['id'],
            'Merk': MEREK_SCALE[laptop['Merk']],
            'ram': SCALE_ram[laptop['ram']],
            'memori_internal': SCALE_memori_internal[laptop['memori_internal']],
            'processor': SCALE_processor[laptop['processor']],
            'layar': SCALE_layar[laptop['layar']],
            'baterai_mah': SCALE_baterai_mah[laptop['baterai_mah']],
            'Harga': SCALE_harga_rp[laptop['Harga']],
        } for laptop in self.dataDict]

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
        harga = [] # min
        for data in self.data:
            Merk.append(data['Merk'])
            ram.append(data['ram'])
            memori_internal.append(data['memori_internal'])
            processor.append(data['processor'])
            layar.append(data['layar'])
            baterai_mah.append(data['baterai_mah'])
            harga.append(data['Harga'])

        max_Merk = max(Merk)
        max_ram = max(ram)
        max_Memori_Internal = max(memori_internal)
        max_processor = max(processor)
        max_layar = max(layar)
        max_baterai_mah = max(baterai_mah)
        min_harga = min(harga)

        return [
            {   'id': data['id'],
                'Merk': data['Merk']/max_Merk, # benefit
                'ram': data['ram']/max_ram, # benefit
                'memori_internal': data['memori_internal']/max_Memori_Internal, # benefit
                'processor': data['processor']/max_processor, # benefit
                'layar': data['layar']/max_layar, # benefit
                'baterai_mah': data['baterai_mah']/max_baterai_mah, # benefit
                'Harga': min_harga/data['Harga'] # cost
                }
            for data in self.data
        ]
 

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id']:
    round(
        row['Merk'] ** weight['Merk'] *
        row['ram'] ** weight['ram'] *
        row['memori_internal'] ** weight['memori_internal'] *
        row['processor'] ** weight['processor'] *
        row['layar'] ** weight['layar'] *
        row['baterai_mah'] ** weight['baterai_mah'] *
        row['Harga'] ** weight['Harga']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))