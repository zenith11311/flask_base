import os, pickle, random

profile = [
          "https://images.unsplash.com/photo-1554440857-e88965a4b51b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        , "https://images.unsplash.com/photo-1553531580-a0868f1263f6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
        , "https://images.unsplash.com/photo-1554453433-9af917b6f571?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        , "https://images.unsplash.com/photo-1554785015-8be8822fa8fc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1400&q=80"
        , "https://images.unsplash.com/photo-1554949886-1275d4fe6699?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        , "https://images.unsplash.com/photo-1554555819-f722cb0c01c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        , "https://images.unsplash.com/photo-1554923155-0e0be630fb5a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        , "https://images.unsplash.com/photo-1554963984-67eb1b95f33f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        , "https://images.unsplash.com/photo-1554967769-1f961137e9c1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        , "https://images.unsplash.com/photo-1554755273-dbcc615878b8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=934&q=80"
        ]

profile_src = [
          "https://unsplash.com/photos/6qkDeIa5UQc"
        , "https://unsplash.com/photos/an_2Dz56gAs"
        , "https://unsplash.com/photos/p797Ju22zvk"
        , "https://unsplash.com/photos/xn02rY4i-NI"
        , "https://unsplash.com/photos/E6ISGswlhSk"
        , "https://unsplash.com/photos/pZTVa_Gt1f8"
        , "https://unsplash.com/photos/fnqDH-yaFWE"
        , "https://unsplash.com/photos/7XlgyctFS3o"
        , "https://unsplash.com/photos/1NPUmTaiMeg"
        , "https://unsplash.com/photos/STPpehNE_OQ"
        ]


def get_users() :

    lst  = list()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    number   = "0123456789"

    for x in range(0, 10) :
        uinfo = dict()

        uinfo['uid'] = ""

        for y in range(0, 4) :
            uinfo['uid'] += random.choice(alphabet)

        uinfo['uid'] += "_"

        for y in range(0, 3) :
            uinfo['uid'] += random.choice(number)

        uinfo['age'] =  ""
        for y in range(0, 2) :
            uinfo['age'] += random.choice(number)

        uinfo['profile']        = profile[x]
        uinfo['profile_src']    = profile_src[x]

        lst.append(uinfo)

    return lst
        
