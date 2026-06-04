review_data = """

reviews.txt

Page
1
/
1
100%
Customer feedback:
- john.doe@example.com
- Phone: +234 803 456 7890
- Another contact: jane_smith@workplace.org
- Alternate phone: +234 701 234 5678
- Feedback: "Great service, will recommend to others."

More feedback:
- michael.brown@yahoo.com
- Phone: +234 909 876 5432
- Comment: "The product quality is excellent."

Customer reviews:
- lucy_liu@shopping.com
- Phone: +234 812 345 6789
- Review: "Fast delivery and good packaging."

Support inquiries:
- support@company.com
- Phone: +234 803 123 4567
- Issue: "Had trouble with my order, but customer support was helpful."

Additional feedback:
- emma_watson@gmail.com
- Phone: +234 805 987 6543
- Comment: "User-friendly website, easy to navigate."

Testimonials:
- robert_downey@hero.com
- Phone: +234 810 234 5678
- Testimonial: "Impressive service and product range."

Client feedback:
- natalie.portman@cinema.org
- Phone: +234 807 654 3210
- Feedback: "Satisfied with my purchase."

Customer response:
- chris_evans@supermail.com
- Phone: +234 806 234 5678
- Comment: "Excellent customer service and fast response."

User reviews:
- scarlett.johansson@movies.net
- Phone: +234 809 876 5432
- Review: "Loved the variety of products available."

Feedback received:
- tom.holland@webslinger.com
- Phone: +234 813 456 7890
- Comment: "Affordable prices and great discounts."
Displaying reviews.txt.
"""

lines = review_data.split("\n")


for line in lines:
    words = line.split()
    print(words)

    