import re
from typing import List


def compare_word_sequences(first_seq: List[str], second_seq: List[str]) -> bool:
    for word in first_seq:
        if word == '':
            continue
        if word in second_seq:
            return True

    return False


def main():
    records: List[str] = ['Equipment ONLY - Lumiere Technologies',
                          'Lumiere Technologies',
                          'Lumiere Tech, Inc.',
                          'Mendes Metal SA - Central Office',
                          '*** DO NOT USE *** Mendes Metal',
                          'Mendes Metal, SA',
                          'Ship to Klapisch Aerospace gmbh',
                          'Klapisch Aero, gmbh Munich',
                          'Klapisch Aerospace tech (use Klapisch Aero, gmbh Munich acct 84719482-A)']
    clean_records: List[str] = []
    passed_records = set()
    for record in records:
        # Skip already passed and evaluated records
        if record in passed_records:
            continue
        record_words = sorted(re.split(';|,|\s', record))
        final_record_name = record
        final_record_words = record_words
        for second_record in records:
            second_record_words = sorted(re.split(';|,|\s', second_record))
            if compare_word_sequences(record_words, second_record_words) is True:
                # Remember similar records, so we can skip them
                passed_records.add(second_record)
                # For final record pick the one with less words
                if len(final_record_words) > len(second_record_words):
                    final_record_name = second_record
                    final_record_words = second_record_words

        clean_records.append(final_record_name)

    print(clean_records)


if __name__ == '__main__':
    main()
