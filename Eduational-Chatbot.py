# Eduational-Chatbot
import sys

class StudentSupportChatbot:
    def __init__(self):
        # Frequently Asked Questions and answers
        self.faq = {
            "what is the admission process": "Our admission process involves submitting an application form, providing transcripts, and attending an interview.",
            "how do i reset my password": "To reset your password, go to the login page and click 'Forgot Password' to receive reset instructions via email.",
            "what courses are offered": "We offer courses in computer science, business administration, psychology, and many other fields. You can find the full list on our website.",
            "how can i contact support": "You can contact support via email at support@university.edu or call us at 912455XXXX.",
            "when does the semester start": "The semester usually starts on the first Monday of September. Please check the academic calendar for exact dates.",
        }

        # Guidance steps for common student processes
        self.guidance = {
            "apply for admission": [
                "Step 1: Complete the online application form.",
                "Step 2: Submit your educational transcripts.",
                "Step 3: Attend the admission interview if invited.",
                "Step 4: Await the admission decision by email."
            ],
            "register for courses": [
                "Step 1: Log in to your student account.",
                "Step 2: Navigate to the course registration section.",
                "Step 3: Select the courses you want to enroll in.",
                "Step 4: Submit your course registration and confirm enrollment."
            ],
            "request transcript": [
                "Step 1: Log in to your student account.",
                "Step 2: Go to the 'Transcript Request' page.",
                "Step 3: Fill out the transcript request form.",
                "Step 4: Submit the request and pay the applicable fees."
            ]
        }

    def greet_user(self):
        print("Hello! I am your Student that Supports Chatbot.")
        print("You can ask me questions, request guidance on student processes, or type 'exit' to leave.")

    def get_response(self, user_input):
        # Normalize input to lower case
        user_input = user_input.lower()

        # Check if input matches FAQ queries
        for question in self.faq:
            if question in user_input:
                return self.faq[question]

        # Check if input relates to guidance processes
        for process in self.guidance:
            if process in user_input:
                return "\n".join(self.guidance[process])

        # Detect if user wants to escalate or complex query keywords
        escalation_keywords = ['human', 'staff', 'representative', 'operator', 'help', 'complex', 'problem']
        if any(word in user_input for word in escalation_keywords):
            return ("I am escalating your issue to our human support staff. "
                    "Please wait while we connect you to a staff member.")

        # Default response if no match
        return ("I'm sorry, I do not have the information to answer that question. "
                "Would you like me to connect you with a human staff member?")

    def run(self):
        self.greet_user()

        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for using the Student Support Chatbot.You can further ask any query in future.Goodbye!")
                break

            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = StudentSupportChatbot()
    chatbot.run()
