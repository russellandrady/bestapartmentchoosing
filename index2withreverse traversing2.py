city = [[0, 1, 0], [1, 0, 0], [1, 1, 0], [0, 1 ,0], [0, 1, 1]]#each aprtments may or may not have gym,school or store
min = 1000
#distance = [[1,0,4],[0,1,3],[0,0,2],[1,0,1],[2,0,0]]
rows = 5
cols = 3
dis = 0
dis2 = 0
distance_matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        for k in range(i, rows):  # Start from the value of i
            # print(k, j)
            if city[k][j] == 0:
                dis += 1
            else:
                if(i>0):
                    for m in range(i, -1, -1):#i-1 indan -1 wenakan adu wegena(-1) yanawa kiyala kiyanne
                        #print(m, j)
                        if city[m][j] == 0:
                            dis2 += 1
                        if city[m][j] == 1:
                            if dis2<dis:
                                dis=dis2
                            break    
                row.append(dis)
                dis2 = 0
                dis = 0
                break
            if(k==rows-1):
                for l in range(i, -1, -1):#i-1 indan -1 wenakan adu wegena(-1) yanawa kiyala kiyanne
                    #print(l, j)
                    if city[l][j] == 0:
                        dis2 += 1
                    if city[l][j] == 1:
                        dis=dis2
                        break
                row.append(dis)
                dis2 = 0
                dis = 0
                break
    distance_matrix.append(row)
#print("Generated Distance Matrix:", distance_matrix)
print("Gym?")
gym = int(input())
print("School?")
school = int(input())
print("Store?")
store = int(input())
for i in range(5):
        calc = gym * distance_matrix[i][0] + school * distance_matrix[i][1] + store * distance_matrix[i][2]
        if calc<min:
            min=calc
            minapart = i#minapart is the apartment that have minimum distance to gym,school and store. But customer can choose whether he want these 3 or not one by one. 
print("The best apartment is",minapart)
