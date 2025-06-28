from retail_analysis import Analysis

def main():
    print("🔍 main.py started")

    level = input("Enter analysis level (Level-1 / Level-2 / Level-3): ").strip().upper()
    valid_levels = ["LEVEL-1", "LEVEL-2", "LEVEL-3"]
    print(f"✅ Level selected: {level}")

    if level not in valid_levels:
        print("❌ Invalid level! Please choose Level-1, Level-2, or Level-3.")
        return
     
       
    file_path = "data/Online Retail .xlsx"

    try:
        print("📦 Creating Analysis object...")
        a = Analysis(level, file_path)
        print("⚙️ Running analysis...")
        a.run_analysis()
        print("✅ Analysis complete. PDF generated.")
    except Exception as e:
        print("prem")
        print(f"❗ Error: {e}")

if __name__ == "__main__":
    main()

    