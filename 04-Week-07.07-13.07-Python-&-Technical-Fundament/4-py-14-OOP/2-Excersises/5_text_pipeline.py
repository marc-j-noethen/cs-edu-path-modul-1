class TextProcessor:
    def __init__(self):
        pass

    def process(self, text):
        raise NotImplementedError("Subclass must implement this method")


class UpperCaseProcessor(TextProcessor):
    def process(self, text):
        return text.upper()


class RemovePunctuationProcessor(TextProcessor):
    def process(self, text):
        translation_table = str.maketrans("", "", ",.!?")
        return text.translate(translation_table)


class Pipeline:
    def __init__(self):
        self.processors = []

    def add_processor(self, processor_object):
        self.processors.append(processor_object)

    def run(self, initial_text):
        text = initial_text
        for processor in self.processors:
            text = processor.process(text)
        return text
