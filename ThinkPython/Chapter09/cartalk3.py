if __name__ == '__main__':
    age = 12
    while age  < 100:
         sage = str(age)
         mom = int(sage[1] + sage[0])
         diff = mom - age
         if diff > 10:
            print age, mom, diff

         age += 1