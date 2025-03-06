def main():
    
    age = int(input("Please enter your age: "))
    max_heart_rate = 220 - age
    min_target = int(max_heart_rate * 0.65)
    max_target = int(max_heart_rate * 0.85)
    
    print("\nWhen you exercise to strengthen your heart, you should")
    print(f"keep your heart rate between {min_target} and {max_target} beats per minute.")

if __name__ == "__main__":
    main()
