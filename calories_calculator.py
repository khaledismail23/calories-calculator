import re


def main():
  info = input_data()
  calories = calculate_calories_before_goal(
      info["weight"],
      info["height"],
      info["age"],
      info["gender"],
      info["activity_level"],
  )
  goal = ""
  while True:
      try:
          goal_input = input("Goal (lose/gain/maintain): ").capitalize()
          if re.search(r"^(Lose|Gain|Maintain)$", goal_input):
              goal = goal_input
              break
      except ValueError:
          pass

  final_calories = calculate_calories_after_goal(goal, calories)
  fcp = fat_carbs_protein_calculator(final_calories, info["weight"])
  bmi = calc_BMI(info["weight"], info["height"])
  results = show_results(
      fcp["protein"],
      fcp["carbs"],
      fcp["fats"],
      bmi,
      final_calories,
      info["first_name"],
      info["last_name"],
      info["gender"],
      info["age"],
      goal,
  )
  print(results)


def input_data():
  info = {}
  while True:
      try:
          first_name = input("First name: ").capitalize()
          if re.search(r"^[A-Z][a-z]+$", first_name):
              info["first_name"] = first_name
              break
      except ValueError:
          pass

  while True:
      try:
          last_name = input("Last name: ").capitalize()
          if re.search(r"^[A-Z][a-z]+$", last_name):
              info["last_name"] = last_name
              break
      except ValueError:
          pass

  while True:
      try:
          weight = int(input("Weight (Kg): "))
          if weight <= 150 and weight >= 35:
              info["weight"] = weight
              break
          else:
              print("please enter a valid number between 35 kg and 150 kg")
      except ValueError:
          pass

  while True:
      try:
          height = int(input("Height (CM): "))
          if height <= 210 and height >= 60:
              info["height"] = height
              break
          else:
              print("please enter a valid number between 60 cm and 210 cm")
      except ValueError:
          pass

  while True:
      try:
          age = int(input("Age (Year): "))
          if age <= 100 and age >= 10:
              info["age"] = age
              break
          else:
              print("please enter a valid number between 10 years and 100 years")
      except ValueError:
          pass

  while True:
      try:
          gender = input("Gender: ").capitalize()
          if re.search(r"^(Male|Female)$", gender):
              info["gender"] = gender
              break
      except ValueError:
          pass

  print("Activity levels:")
  print("1) Sedentary (little or no exercise)")
  print("2) Lightly Active (light exercise / sports 1-3 days a week)")
  print("3) Moderately Active(moderate exercise / sports 3-5 days a week)")
  print("4) Very Active(hard exercise / sports 6-7 days a week)")
  print("5) Extra Active(very hard exercise / sports & physical job or 2x training)")
  while True:
      try:
          activity_level = int(input("Activity level: "))
          if activity_level in [1, 2, 3, 4, 5]:
              info["activity_level"] = activity_level
              break
          else:
              print("please enter a valid number between 1 and 5")
      except ValueError:
          pass

  return info


def calculate_calories_before_goal(weight, height, age, gender, activity_level):
  bmr = 0
  if gender == "Male":
      bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
  else:
      bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

  calories = 0
  if activity_level == 1:
      calories = bmr * 1.2
  elif activity_level == 2:
      calories = bmr * 1.375
  elif activity_level == 3:
      calories = bmr * 1.55
  elif activity_level == 4:
      calories = bmr * 1.725
  elif activity_level == 5:
      calories = bmr * 1.9

  return calories


def calculate_calories_after_goal(goal, calories):
  if goal == "Gain":
      while True:
          try:
              years_of_exp = float(input("Years of experience: "))
              if years_of_exp >= 0 and years_of_exp < 2:
                  return calories + 400
              elif years_of_exp >= 2 and years_of_exp < 5:
                  return calories + 300
              elif years_of_exp >= 5 and years_of_exp < 6:
                  return calories + 200
              elif years_of_exp >= 6:
                  return calories + 100
          except ValueError:
              pass
  elif goal == "Lose":
      while True:
          try:
              amount = float(
                  input(
                      "How much you want to lose per week? 0.25(kg/week), 0.5(kg/week) 1(kg/week): "
                  )
              )
              if amount in [0.25, 0.5, 1]:
                  if amount == 0.25:
                      return calories * 0.91
                  elif amount == 0.5:
                      return calories * 0.81
                  elif amount == 1:
                      return calories * 0.63
                  else:
                      print("please enter a valid amount from (0.25, 0.5, 1)")
          except:
              pass
  elif goal == "Maintain":
      return calories


def fat_carbs_protein_calculator(calories, weight):
  protein_amount = 2.2 * weight
  protein_calories = protein_amount * 4
  fats_calories = calories * 0.2
  fats_amount = fats_calories / 9
  carbs_calories = calories - protein_calories - fats_calories
  carbs_amount = carbs_calories / 4

  return {"protein": protein_amount, "fats": fats_amount, "carbs": carbs_amount}


def calc_BMI(weight, height):
  return weight / (height / 100) ** 2


def show_results(protein, carbs, fats, bmi, calories, first, last, gender, age, goal):
  title = ""
  if gender == "Male":
      title = "Mr."
  else:
      title = "Ms."

  weight_category = ""
  if bmi <= 18.5:
      weight_category = "Underweight"
  elif bmi > 18.5 and bmi < 25:
      weight_category = "Normal weight"
  elif bmi >= 25 and bmi < 30:
      weight_category = "Overweight"
  elif bmi >= 30:
      weight_category = "Obesity"

  return f"""Final Results for {title} {first} {last}, ({age} years old):
  1) your BMI is {bmi:.02f} and your weight category is {weight_category}.
  2) total calories required per day in order to {goal} weight is ({calories:.02f} calories) divided into ({protein:.02f} g of protein / {carbs:.02f} g of carbs / {fats:.02f} g of fats)."""


if __name__ == "__main__":
  main()
