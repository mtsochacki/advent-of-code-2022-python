def part1(buffer):
    chunks = []
    for i in range(0, len(buffer), 1):
        chunks.append(buffer[i:i + 4])
    start_of_packet = 0
    for chunk in chunks:
        set_of_chunk_characters = set(chunk)
        print(set_of_chunk_characters)
        if len(set_of_chunk_characters) == 4:
            start_of_packet = buffer.find(chunk)
            break
    return start_of_packet + 4

def part2(buffer):
    chunks = []
    for i in range(0, len(buffer), 1):
        chunks.append(buffer[i:i + 14])
    start_of_packet = 0
    for chunk in chunks:
        set_of_chunk_characters = set(chunk)
        print(set_of_chunk_characters)
        if len(set_of_chunk_characters) == 14:
            start_of_packet = buffer.find(chunk)
            break
    return start_of_packet + 14


if __name__ == '__main__':
    datastream_buffer = open("../resources/day06.txt").read()
    print(part1(datastream_buffer))
    print(part2(datastream_buffer))