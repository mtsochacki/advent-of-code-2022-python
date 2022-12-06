def look_for_packet(buffer, length):
    chunks = []
    for i in range(len(buffer)):
        chunks.append(buffer[i:i + length])
    for chunk in chunks:
        set_of_chunk_characters = set(chunk)
        if len(set_of_chunk_characters) == length:
            return buffer.find(chunk) + length


if __name__ == '__main__':
    datastream_buffer = open("resources/day06.txt").read()
    print(look_for_packet(datastream_buffer, 4))
    print(look_for_packet(datastream_buffer, 14))
