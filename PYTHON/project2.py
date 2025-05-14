import pandas as pd

# Load the dataset
DATA_PATH = "C:\\Users\\User\\Desktop\\PROJECT 2\\input\\CAR DETAILS FROM CAR DEKHO.csv"
df = pd.read_csv(DATA_PATH)

# ✅ Define reliable brands for low maintenance
RELIABLE_BRANDS = ["Maruti", "Toyota", "Hyundai"]

# ✅ Define luxury brands
LUXURY_BRANDS = ["Audi", "Mercedes", "BMW"]

# Function to recommend cars based on user input
def recommend_car(price, fuel_type, seller_type, owner_types, transmission_types, low_maintenance, luxury_preference):
    if not isinstance(owner_types, list):
        owner_types = [owner_types]  # Ensure owner_types is a list

    if not isinstance(transmission_types, list):
        transmission_types = [transmission_types]  # Ensure transmission_types is a list

    # ✅ Step 1: Convert price to actual price range
    max_price = price * 100000 * 1.1  # Allow 10% buffer
    min_price = 50000  # Minimum price of ₹50,000

    # ✅ Step 2: Filter cars based on price FIRST
    filtered_cars = df[
        (df['selling_price'].astype(float) <= max_price) & 
        (df['selling_price'].astype(float) >= min_price)
    ]

    # ✅ Step 3: Apply remaining filters, including transmission type
    filtered_cars = filtered_cars[
        (filtered_cars['fuel'].str.strip().str.lower() == fuel_type.strip().lower()) &
        (filtered_cars['seller_type'].str.strip().str.lower() == seller_type.strip().lower()) &
        (filtered_cars['owner'].isin(owner_types)) &
        (filtered_cars['transmission'].isin(transmission_types))  # ✅ Filter based on transmission
    ]

    # ✅ Step 4: Apply low maintenance filter if selected
    if low_maintenance.lower() == "yes":
        filtered_cars = filtered_cars[filtered_cars['name'].str.contains('|'.join(RELIABLE_BRANDS), case=False, na=False)]

    # ✅ Step 5: Apply luxury car filter if selected
    if luxury_preference.lower() == "yes":
        filtered_cars = filtered_cars[filtered_cars['name'].str.contains('|'.join(LUXURY_BRANDS), case=False, na=False)]

    # ✅ Step 6: Handle empty results
    if filtered_cars.empty:
        return pd.DataFrame({"message": ["❌ No matching cars found. Try different filters!"]})

    return filtered_cars.head(5)  # Return top 5 results

# Test the function
if __name__ == "__main__":
    print("Beginner Driver Recommendations (Automatic only, Low Maintenance):")
    print(recommend_car(10, "Petrol", "Dealer", ["First Owner"], ["Automatic"], "Yes", "No"))

    print("\nExperienced Driver Recommendations (Automatic & Manual, All Brands):")
    print(recommend_car(10, "Petrol", "Dealer", ["Second Owner", "Third Owner", "Fourth & Above Owner"], ["Automatic", "Manual"], "No", "No"))

    print("\nLuxury Car Recommendations:")
    print(recommend_car(50, "Petrol", "Dealer", ["First Owner", "Second Owner"], ["Automatic", "Manual"], "No", "Yes"))
