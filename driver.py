driver = input('Did you drive a car? (Yes or No)')
age = input('How old are you?')
age = int(age)
if driver == 'Yes':
	if age >= 18:
		print('Good job!')
	else:
		print('Why did you drive the car?')
elif driver == "No":
	if age >= 18:
		print('You can get a driver lisence')
	else:
		print('Good, you can get one lisence after many years')
else:
	print('Only type Yes or No plz!')
	raise SystemExit