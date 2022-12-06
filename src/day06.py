def look_for_packet(buffer, length):
    for i in range(len(buffer)):
        if len(set(buffer[i:i + length])) == length:
            return i + length


if __name__ == '__main__':
    datastream_buffer = open("resources/day06.txt").read()
    print(look_for_packet(datastream_buffer, 4))
    print(look_for_packet(datastream_buffer, 14))
