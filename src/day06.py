def part1(buffer):
    return look_for_packet(buffer, 4)


def part2(buffer):
    return look_for_packet(buffer, 14)


def look_for_packet(buffer, length):
    chunks = []
    for i in range(0, len(buffer), 1):
        chunks.append(buffer[i:i + length])
    start_of_packet = 0
    for chunk in chunks:
        set_of_chunk_characters = set(chunk)
        if len(set_of_chunk_characters) == length:
            start_of_packet = buffer.find(chunk)
            break
    return start_of_packet + length


if __name__ == '__main__':
    datastream_buffer = open("../resources/day06.txt").read()
    print(part1(datastream_buffer))
    print(part2(datastream_buffer))
