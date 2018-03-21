
"""
这个算法的内容为贪婪算法，用该算法可以实现覆盖问题
其中用到了集合的部分，交集、并集、差集
得到的东西是近似解

"""
#需要覆盖的州

states_needed = set(["mt", "wa", "or", "id", "nv","ut","ca","az"])

#广播台清单
stations = {}
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa" , "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#存储最终选择的广播台
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)
print(final_stations)
