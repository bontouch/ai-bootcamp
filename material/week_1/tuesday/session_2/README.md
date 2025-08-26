# Receipt Expense Categorization Lab

## Learning Objectives

- Master few-shot prompting techniques for domain-specific categorization
- Understand how examples guide LLM behavior for consistent outputs
- Build structured data extraction pipelines with validation
- Experience the power of prompt engineering for business logic

## The Challenge

Build a receipt processing system that automatically categorizes purchases into expense categories. The key challenge: **categorization requires business context that isn't obvious from item names alone**.

Without proper examples, an LLM might categorize items inconsistently. Your task is to use **few-shot prompting** to teach the model the categorization rules.

## Task Overview

Create a system that:

1. **Extracts structured data** from receipt text using OpenAI's structured outputs
2. **Categorizes each item** into one of four expense categories:
   - Food & Beverage
   - Health & Wellness
   - Household & Utilities
   - Leisure & Entertainment
3. **Validates financial calculations** (subtotal + tax = total)
4. **Displays categorized results** with item lists for each category

## Expected Deliverable

Your system should process the sample receipt (provided in `sample_receipt.txt`) and produce categorized output:

**Sample Receipt Preview:**
```
DOWNTOWN CONVENIENCE STORE RECEIPT
March 16, 2024 - 14:32

3x Cappuccino Large         78 SEK
1x Protein Smoothie         65 SEK
2x Energy Drinks            70 SEK
1x Vitamin C Supplements    125 SEK
1x Yoga Mat                 299 SEK
1x Essential Oils Set       149 SEK
...and 14 more items

Total: 2837 SEK
```

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
Use OpenAI's `client.beta.chat.completions.parse()` with your Pydantic models for guaranteed structure.

## The Few-Shot Challenge

**These items are deliberately ambiguous:**
- Energy Drinks (Food or Health?)
- Essential Oils (Health or Household?)
- Hand Sanitizer (Health or Household?)
- Bluetooth Headphones (Leisure or Health for work calls?)
- Journal (Leisure or Health for wellness?)

Your few-shot examples must establish clear rules for these edge cases.

## Implementation Tips

1. **Start with the prompt** - Get categorization working first
2. **Add validation** - Catch AI calculation errors
3. **Test edge cases** - Try ambiguous items in interactive mode
4. **Iterate on examples** - Refine your few-shot prompts based on results

## Files Provided

- `sample_receipt.txt` - Sample receipt with 20 ambiguous items to process
- `starter_code/models.py` - Template for Pydantic models (TODO: implement)
- `starter_code/extractor.py` - Template for OpenAI integration (TODO: implement)
- `starter_code/main.py` - Template for CLI interface (TODO: implement)
- `starter_code/.env.example` - Environment variable template

## Getting Started
```bash
uv add openai pydantic python-dotenv
export OPENAI_API_KEY="your-key"
python main.py
```

## Success Criteria

✅ **Consistent categorization** - Same item types always go to same category  
✅ **Financial validation** - Math errors caught by Pydantic validators  
✅ **Few-shot prompting** - Clear examples guide model behavior  
✅ **Interactive testing** - Can process custom receipts  
✅ **Clean output** - Categorized items displayed clearly  

## Time Estimate

**3 hours** - Focus on getting the few-shot prompting right. The technical implementation is straightforward, but crafting effective examples takes iteration.

---

*This lab demonstrates why few-shot prompting is essential for production AI applications - without examples, even simple categorization becomes inconsistent.*