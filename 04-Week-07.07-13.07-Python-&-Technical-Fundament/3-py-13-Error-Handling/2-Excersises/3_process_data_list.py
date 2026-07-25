def process_data_list(data):
    total = 0.0

    for item in data:
        try:
            reciprocal = 1.0 / item
            total += reciprocal
        except (TypeError, ZeroDivisionError) as error:
            print(f"Error processing {item}: {str(error)}")
        finally:
            print(f"Finished processing item: {item}")

    return total
