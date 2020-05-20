# import country

# country = country.worldwide()

# # li = country.country_list()
# # dictr = country.worldwide_data()
# # dictr = country.get_country_data("india")
# li = country.get_state_data("us",state="California")
# f = open("abc.txt","w")
# for i in li:
#     f.write(str(i)+"\n")
# f.close()

import time
a=10
b =20
l=[1,2,3]
l2=[1,2,3]
print(a is b)
print(l is l2)
li=list(range(10000))
li2=list(range(700,860))
li.extend(list(range(700,770)))
li.extend(li2)
start = time.time()
# maxi = max(set(li),key = li.count)
li2=[]
end = time.time()
print(end-start)