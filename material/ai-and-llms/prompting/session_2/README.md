# Receipt Expense Categorization Lab

## Learning Objectives

- Master few-shot prompting techniques for domain-specific categorization
- Understand how examples guide LLM behavior for consistent outputs
- Build structured data extraction pipelines with validation

## The Challenge

Build a receipt processing system that automatically categorizes purchases into expense categories. The key challenge: **categorization requires business context that isn't obvious from item names alone**. Without proper examples, an LLM might categorize items inconsistently. Practice on using **few-shot prompting** to teach the model the categorization rules.

## Task Overview

Create a system that:

1. **Extracts structured data** from receipt text using structured outputs
2. **Categorizes each item** into one of four expense categories:
   - Food & Beverage
   - Health & Wellness
   - Household & Utilities
   - Leisure & Entertainment
3. **Validates financial calculations** (subtotal + tax = total)
4. **Displays categorized results** with item lists for each category

## Expected Deliverable

Your system should process the sample receipt (provided in `sample_receipt.txt`) and produce categorized output:

**Expected Output:**
```
Sample Receipt: SUCCESS - Confidence: 0.95
Total: SEK 2837
Items: 20
Expense Categories (4):
  • Food & Beverage: SEK 253 (5 items)
    - 3x Cappuccino Large
    - 1x Protein Smoothie
    - 2x Energy Drinks
    - 2x Herbal Tea
    - 1x Protein Bars (6-pack)
  • Health & Wellness: SEK 768 (4 items)
    - 1x Vitamin C Supplements
    - 1x Yoga Mat
    - 1x Essential Oils Set
    - 1x Massage Oil
  • Household & Utilities: SEK 330 (4 items)
    - 1x Laundry Detergent
    - 1x Hand Sanitizer
    - 1x Cleaning Wipes
    - 1x Air Purifier Filters
  • Leisure & Entertainment: SEK 1014 (7 items)
    - 1x Board Game (Monopoly)
    - 1x Streaming Gift Card
    - 1x Bluetooth Headphones
    - 1x Journal
    - 1x Puzzle (1000 pieces)
    - 1x Phone Charger
    - 1x Scented Candles
```

## Key Technical Requirements

### 1. Pydantic Models
- `Receipt` model with line items, totals, and expense categories
- `ExpenseCategory` model with category name, total, count, and item list
- `LineItem` model with validation for quantity × unit_price = total_price
- Financial validation: subtotal + tax_amount = total_amount

### 2. Few-Shot Prompting
Your prompt must include **concrete examples** that teach the model:
- How to categorize ambiguous items (e.g., "Energy Drinks" → Food & Beverage)
- Business logic for edge cases (e.g., "Essential Oils" → Health & Wellness)
- Consistent category naming

### 3. Structured Outputs
Use OpenAI's `client.responses.parse()` with your Pydantic models for guaranteed structure.

## The Few-Shot Challenge

**These items are deliberately ambiguous:**
- Energy Drinks (Food or Health?)
- Essential Oils (Health or Household?)
- Hand Sanitizer (Health or Household?)
- Bluetooth Headphones (Leisure or Health for work calls?)
- Journal (Leisure or Health for wellness?)

## Running the script
```bash
uv add openai pydantic python-dotenv
export OPENAI_API_KEY="your-key"
python main.py
```
