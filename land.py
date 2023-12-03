class Land:
    def __init__(self, index): #index为类型序号，0河流 1河边草地 2平原草地 3平原森林 4高山草地 5高山荒地
        self.index = index
        match self.index:
            case "0":
                self.land_type = river
            case "1":
                self.land_type = riverside_meadow #类型名称
                self.qualt_H2O = 1.5 #水量因子
                self.qualt_resc = 1 #资源量因子
                self.qualt_metbls = 1.2 #代谢率因子
            case "2":
                self.land_type = plain_meadow
                self.qualt_H2O = 1
                self.qualt_resc = 1
                self.qualt_metbls = 1
            case "3":
                self.land_type = plain_forest
                self.qualt_H2O = 1
                self.qualt_resc = 1.5
                self.qualt_metbls = 1.2
            case "4":
                self.land_type = mountain_meadow
                self.qualt_H2O = 0.8
                self.qualt_resc = 0.8
                self.qualt_metbls = 0.6
            case "5":
                self.land_type = mountain_desert
                self.qualt_H2O = 0.6
                self.qualt_resc = 0.1
                self.qualt_metbls = 0.3
        self.orig_soil_H2O = self.qualt_H2O * 10 #初始土壤水
        self.orig_soil_C = self.qualt_resc * 10 #初始土壤碳
        self.orig_plant_C = self.qualt_resc * 5 #初始植物碳
        self.prodc_rate = self.qualt_resc * self.qualt_H2O * 1 #光合作用生产有机物速率
        self.respr_rate = self.qualt_metbls * 0.5 #呼吸作用消耗有机物速率