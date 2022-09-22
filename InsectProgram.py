import InsectJawn as i

#This creates 2 separate instances, housefly and mosquito
housefly = i.Insect(2,4)
mosquito = i.Insect(4,8)

housefly.calc_flight()
mosquito.calc_flight()



print("the housefly can fly up to", housefly.get_flight())
print("the mosquito can fly up to ", mosquito.get_flight())