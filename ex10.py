class TestPhrase:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        print("Enter text shorter than 15 characters")
        assert len(phrase) < 15, f"Phrase longer than 15 characters"
