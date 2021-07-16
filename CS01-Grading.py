S1 = int(input('คะแนนเก็บ: '))
S2 = int(input('คะแนนสอบกลางภาค: '))
S3 = int(input('คะแนนสอบปลายภาค: '))

Score = S1 + S2 + S3

if(S1 > 30) or (S2 > 30) or (S3 > 40) or (Score > 100):
    print("Enter the real score plese")
else:
    print("Your total score is ",Score)




    if(Score >= 80) and (Score <= 100):
        print("Grade A")
    elif(Score >= 75) and (Score <=79):
        print("Grade B+")
    elif(Score >=70) and (Score <=74):
        print("Grade B")
    elif(Score >=65) and (Score <=69):
        print("Grade C+")
    elif(Score >=60) and (Score <=64):
        print("Grade C")
    elif(Score >=55) and (Score <=59):
        print("Grade D+")
    elif(Score >=50) and (Score <=54):
        print("Grade D")
    elif(Score >=0) and (Score <=49):
        print("Grade F")