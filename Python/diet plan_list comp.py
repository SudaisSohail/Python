healthy_foods = ["carrot" , "cucumber" , "cereals" , "mutton" , "fish" , "lady finger" , "garlic" , "broccoli" , "wheat" , "rice", "fruits"]
kitchen = ["pizza" , "burger" , "cucumber" , "cereals" , "mutton" , "french fries" , "cakes" , "biscuits" , "chips" , "broiler chicken" ,
"sweets" , "wheat" , "rice" , "lasagna" , "fruits"]
kitchen.append("fast foods")
kitchen.remove('pizza')
kitchen.remove('burger')
kitchen.remove('lasagna')
kitchen.remove('french fries')

foods_to_be_eaten = [food.upper() for food in kitchen if food in healthy_foods]
foods_not_to_be_eaten = [foods.upper() for foods in kitchen if foods not in healthy_foods]
foods_to_be_bought = [items.upper() for items in healthy_foods if items not in kitchen]

print("You should eat these:" , foods_to_be_eaten , '\n' + '----------------------------------------------------------------------------------------------------------')
print("You should try to avoid these:" , foods_not_to_be_eaten , '\n' + "----------------------------------------------------------------------------------------------------------")
print("You should buy these:" , foods_to_be_bought , "\n" + "----------------------------------------------------------------------------------------------------------")