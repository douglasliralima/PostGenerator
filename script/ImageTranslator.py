import pytesseract
from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator

# Initialize the translator
translator = Translator()

def extract_sentences_with_positions(image_path):
    """
    Extract sentences and their bounding box positions from the image.
    Group words into sentences based on delimiters (e.g., ".", "?", "!").
    """
    try:
        img = Image.open(image_path)
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

        sentences = []
        current_sentence = {"text": "", "box": None}

        for i in range(len(data["text"])):
            word = data["text"][i].strip()
            if not word:  # Skip empty text
                continue

            x, y, width, height = data["left"][i], data["top"][i], data["width"][i], data["height"][i]

            # Initialize or expand the bounding box for the sentence
            if current_sentence["box"] is None:
                current_sentence["box"] = [x, y, x + width, y + height]
            else:
                current_sentence["box"][2] = max(current_sentence["box"][2], x + width)
                current_sentence["box"][3] = max(current_sentence["box"][3], y + height)

            # Add the word to the current sentence
            current_sentence["text"] += f" {word}"

            # If the word ends a sentence, finalize the sentence
            if word.endswith((".", "?", "!")):
                sentences.append(current_sentence)
                current_sentence = {"text": "", "box": None}

        # Add the last sentence if any
        if current_sentence["text"]:
            sentences.append(current_sentence)

        return sentences
    except Exception as e:
        print(f"Error extracting sentences: {e}")
        return []

def translate_text(text, target_language="es"):
    """
    Translate the text into the target language using Google Translate.
    """
    try:
        if not text.strip():  # Skip if the text is empty
            return text
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text  # Return the original text if translation fails


def replace_sentences_in_image(image_path, sentences, output_path, target_language="es"):
    """
    Replace sentences in the image at the same positions with translated text.
    """
    try:
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)

        # Use a specific font (adjust path as needed)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=20)

        for sentence in sentences:
            text = sentence["text"].strip()
            box = sentence["box"]
            

            # Translate the sentence
            translated_text = translate_text(text, target_language)
            

            # Extract bounding box dimensions
            x1, y1, x2, y2 = box

            # Clear the original text area by drawing a rectangle
            draw.rectangle([x1, y1, x2, y2], fill="white")

            # Place the translated sentence in the same position
            draw.text((x1, y1), translated_text, fill="black", font=font)

        # Save the updated image
        img.save(output_path)
        print(f"Translated image saved at {output_path}")
    except Exception as e:
        print(f"Error replacing sentences in image: {e}")

if __name__ == "__main__":
    # Input image path
    image_path = "input_image.jpg"
    output_path = "output_image.jpg"

    # Step 1: Extract sentences and positions
    sentences = extract_sentences_with_positions(image_path)

    # Step 2: Replace sentences in the image with translations
    replace_sentences_in_image(image_path, sentences, output_path, target_language="es")
