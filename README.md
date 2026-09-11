# alu-regex-data-extraction

## Overview
This program extracts and validates hashtags, emails, phone numbers, and credit card numbers from raw text data using regex, with security checks to detect fake or malicious data.

## How to Run
1. Navigate into the project folder: `cd alu-regex-data-extraction_Elham-cyber780`
2. Navigate into the src folder: `cd src`
3. Run the program: `python main.py`

Output is automatically saved to `output/sample-output.json`.

## Data Types Extracted
- **Hashtags** — starts with `#`, followed by one or more letters only (no numbers, no spaces).
- **Local phone numbers** — starts with `0`, followed by exactly 9 more digits (10 digits total).
- **International/WhatsApp phone numbers** — starts with `+250`, followed by 9 digits, optionally separated by dashes.
- **Credit card numbers** — exactly 16 digits, grouped in 4s, separated by spaces, dashes, or no separator at all.
- **Regular email addresses** — username (letters, numbers, dots) followed by `@`, a domain (letters only), a dot, and an extension (letters only). Example: `name@gmail.com`.
- **ALU official emails** — specifically ends with `@alueducation.com`.
- **ALU alumni emails** —  specifically ends with `@alumni.alueducation.com`.
- **ALU SI emails** — specifically ends with `@si.alueducation.com`.

## Security & Validation Approach
- Credit card numbers and phone numbers with all-repeating digits (e.g. `0000000000`) are flagged and rejected as likely fake/placeholder data.
- Text resembling script injection attempts (e.g. `<script>` tags) is detected, regardless of upper/lowercase, and flagged as a security concern.
- Valid credit card numbers are masked in the output, showing only the last 4 digits (e.g. `**** **** **** 4471`), to protect sensitive data and user's security.

## Known Limitations
- The general email pattern does not fully capture ALU subdomain emails (alumni/si) since it stops at the first dot — separate dedicated patterns were built for `alumni.alueducation.com` and `si.alueducation.com` to handle this correctly.
- Hashtags and usernames containing underscores (e.g. `#act_now`) are only partially matched, since underscore was intentionally left out of the letter/number character set.