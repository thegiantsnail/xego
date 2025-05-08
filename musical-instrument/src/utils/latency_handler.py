def calculate_latency(start_time, end_time):
    return end_time - start_time

def adjust_for_latency(audio_stream, latency):
    if latency > 0:
        audio_stream.delay(latency)  # Adjust the audio stream for latency

def measure_latency(audio_stream):
    start_time = audio_stream.get_time()
    # Simulate audio processing
    end_time = audio_stream.get_time()
    return calculate_latency(start_time, end_time)