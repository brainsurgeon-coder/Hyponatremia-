# This is a programme to manage hyponatremia

print("*".center(80, '*'))
print("Hi! Welcome to Hyponatremia evaluation tool -  Copyright Dr Hrishikesh Sarkar")
print()
print("*".center(80, '*'))

while True:
    try:
        input1 = input("Enter serum osmolality in mOsm/Kgs: ")
        input1 = int(input1)
        if input1 < 100:
            print("Check values - Too low for the range.")
        elif input1 > 400:
            print("Check values - Too high for the range.")
        else:
            break

    except ValueError:
        print("No valid integer! Please retry.")

if input1 <= 275:
    print("This is a hypotonic hyponatremia.")
    x = int(input("Enter urine osmolality in mOSm/Kgs: "))
    if x < 100:
        print("Its water intoxication or psychogenic polydipsia.")
    else:
        print("Inappropriately concentrated urine.")
        print("Enter \n 1 if volume status is depleted,\n 2 if it is normal and \n 3 if increased")
        y = int(input("Enter volume status code here: "))
        if y ==1:
            #print("Enter Urinary sodium.")
            z =int(input("Urinary sodium:\n "))
            if z > 20:
                print("Possible caused of low sodium are, Renal loss, Cerebral salt wasting, Diuretics, Addisonian.")
            else:
                print("Extrarenal loss")
        elif y == 2:
            print("Possible caused of low sodium are SIADH, K+ Loss, Endocrinopathy")
        elif y == 3:
            #print("Enter urinary sodium:")
            z = int(input("Urinary sodium:\n "))
            if z > 20:
                print("The most likely cause of  low sodium is renal failure")
            else:
                print("Likely cause of low sodium is Congestive heart failure or cirrhosis.")
elif input1 > 290:
    print ("This is a hypertonic hyponatremia. Causes - Hyperglycemia / Mannitol Therapy")
else:
    print("This is isotonic hyponatremia. Causes - Paraproteinemia, Hypertriglyceridemia")
print()        
print("That's the end of this evaluation.")
print("*".center(80, '*'))
