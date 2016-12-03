def display_movie(m):
    print("Original name:",m["org_name"])
    print("Translated name:",m["trans_name"])
    print("Year:",m["year"])
    print()
def create_movie(org_name,trans_name,year):
    return {
        "org_name": org_name,
        "trans_name": trans_name,
        "year": year
        }
movie0=create_movie("The hunger game", "Dau truong sinh tu", 2016)
##display_movie(movie0)


def display_movie_list(m_list):
    n=0    
    for i in m_list:
        print("Movie#{0}".format(n+1))
        print("Original name:",i["org_name"])
        print("Translated name:",i["trans_name"])
        print("Year:",i["year"])
        print()
        n+=1
        
movie_list=[]
movie1=create_movie("Little Door Gods", "Tieu Mon Than", 2015)
movie_list.append(movie0)
movie_list.append(movie1)

display_movie_list(movie_list)

def remove_movie(m_list,movie):
    if movie == m_list[0]:
        m_list=m_list[1]
    else:
        m_list = m_list[0]
    return [m_list]

movie_list = remove_movie(movie_list,movie0)

display_movie_list(movie_list)

def search_movie_by_year(m_list,year):
    new_list = []
    for i in m_list:
        if i["year"]==year:
            new_list.append(i)
    return new_list

movie_list = []
movie_list.append(create_movie("The hunger game", "Dau truong sinh tu", 2016))
movie_list.append(create_movie("Break point", "Ranh gioi chet", 2015))
movie_list.append(create_movie("Little Door Gods", "Tieu Mon Than", 2015))
movie_in_2015=search_movie_by_year(movie_list,2015)
##print(movie_in_2015)
display_movie_list(movie_in_2015)


