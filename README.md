# Automation_Product_Price_Alert_Email
A Python script that monitors Amazon product prices based on URLs listed in input.csv and sends automated email notifications when a product reaches its target price.

## Description
This project is a Python-based script that monitors product prices from Amazon and automatically sends email notifications when a product reaches its target price. The system helps users track price drops efficiently.

## Features
- Monitor Amazon product prices.
- Read product URLs and target prices from `input.csv`.
- Automatically send email notifications when a product price reaches or drops below the target price.
- Configurable email settings for personalized notifications.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Lekha03/Automation_Product_Price_Alert_Email.git
   cd Automation_Product_Price_Alert_Email
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up email configuration in `.env` file:
   ```plaintext
   EMAIL_HOST=smtp.example.com
   EMAIL_PORT=587
   EMAIL_USERNAME=your_email@example.com
   EMAIL_PASSWORD=your_email_password
   ```
4. Add product URLs and target prices to `input.csv` in the following format:
   ```csv
   product_url,target_price
   https://www.amazon.com/dp/B08N5WRWNW,499.99
   ```
5. Run the script:
   ```bash
   python script.py
   ```

## Usage
1. Ensure `input.csv` contains the product URLs and target prices.
2. The script will check prices periodically and send an email when a price matches or falls below the target.
3. Email notifications include product details and a direct purchase link.

## Configuration
- Update email settings in `.env`.
- Modify `script.py` to customize scraping logic or add more features.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any issues or suggestions, please open an issue on the repository or email `l2studiosubusiness@gmail.com`.


