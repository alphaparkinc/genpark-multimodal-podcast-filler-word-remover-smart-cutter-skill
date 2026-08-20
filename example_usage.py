from client import MultimodalPodcastFillerWordRemoverSmartCutterClient

def main():
    client = MultimodalPodcastFillerWordRemoverSmartCutterClient()
    res = client.process_podcast(target_clip_count=2)
    print(f"Filler Words Removed: {res['filler_words_removed_count']}")
    print(f"Dead Air / Silence Trimmed: {res['time_saved_seconds']}s")
    print("Extracted Viral Clips:")
    for c in res["viral_clip_timestamps"]:
        print(f"  - [{c['start_time']} -> {c['end_time']}] (Virality {c['virality_score']}/10): {c['hook_text']}")

if __name__ == "__main__":
    main()
