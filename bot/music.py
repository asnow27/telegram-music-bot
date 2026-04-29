"""
Music player functionality
"""

import logging

logger = logging.getLogger(__name__)


class MusicPlayer:
    """
    Handles music playback and queue management
    """

    def __init__(self):
        """
        Initialize the music player
        """
        self.queue = []
        self.current_song = None
        self.is_playing = False

    def play(self, song: str) -> bool:
        """
        Play a song

        Args:
            song: Song name or URL

        Returns:
            True if successful, False otherwise
        """
        logger.info(f'Playing: {song}')
        self.current_song = song
        self.is_playing = True
        return True

    def stop(self) -> bool:
        """
        Stop playback

        Returns:
            True if successful, False otherwise
        """
        logger.info('Stopping playback')
        self.is_playing = False
        self.current_song = None
        return True

    def add_to_queue(self, song: str) -> bool:
        """
        Add a song to the queue

        Args:
            song: Song name or URL

        Returns:
            True if successful, False otherwise
        """
        self.queue.append(song)
        logger.info(f'Added to queue: {song}')
        return True

    def get_status(self) -> dict:
        """
        Get current player status

        Returns:
            Dictionary with status information
        """
        return {
            'is_playing': self.is_playing,
            'current_song': self.current_song,
            'queue_length': len(self.queue)
        }
