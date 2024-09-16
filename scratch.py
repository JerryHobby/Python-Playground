def books():
    return "0.Fantasy, 1.Science_Fiction, 2.Historical_Fiction, 3.Mystery, 4.Horror, 5.Romance_Novel, 6.Literary_Fiction, 7.Memoir, 8.Thriller, 9.Adventure_Fiction, 10.Magical_Realism, 11.Children's_Literature, 12.Contemporary_Fantasy, 13.Dystopian_Fiction, 14.Young_Adult, 15.Fairytale, 16.Fiction, 17.Romantic_Suspense, 18.Women's_Fiction, 19.Graphic_Novels, 20.History, 21.Short_Story, 22.Crime_Fiction, 23.Erotic_Romance_Novels"

print("Are you a BOOKS/NOVELS person? TRUE or FALSE!")
ans1 = str(input())
print( ans1.capitalize() )

if ans1 == "True":
    print(books())

elif ans1 == "False" :
    print("Oh!No worries.")