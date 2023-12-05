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
        ###水循环部分
        self.orig_soil_H2O = self.qualt_H2O * 10 #初始土壤水，标准为10
        self.evapo_rate = self.orig_soil_H2O * 0.1 #蒸发速率，为0.1倍水量
        self.flow_rate = 0.5 * self.orig_soil_H2O * 0.1 #径流速率，为概率0.5的0.1倍水量
        self.rain_rate = 1 #如有降雨则降雨速率为1
        ###碳循环部分
        self.orig_plant_C = self.qualt_resc * 10 #初始植物碳，标准为10
        self.prodc_rate = self.qualt_resc * self.qualt_H2O * 1 #光合作用生产植物有机物速率，标准为1
        self.respr_rate = self.qualt_metbls * 0.5 #呼吸作用消耗植物有机物速率，标准为0.5
        self.fallin_rate = 0.5 * self.qualt_metbls * 0.1 #死亡/掉落消耗植物有机物速率，标准的0.5概率的0.1
        self.orig_soil_C = self.qualt_resc * 10 #初始土壤碳，标准为10
        self.decom_rate = self.qualt_metbls * 0.1 #分解作用消耗土壤有机物速率，标准为0.1
        
class air:
    def __init__(self):
        self.orig_air_H2O = 1000 #初始大气水
        self.orig_air_C = 1000 #初始大气碳
        #水汽输送（水量补充）速率

#径流函数
#降水函数
#蒸发作用函数

#光合作用函数（植物&大气
#呼吸作用函数（植物&大气
#死亡掉落函数（植物&土壤
#分解作用函数（土壤&大气
