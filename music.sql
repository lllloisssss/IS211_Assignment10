-- music.sql
-- IS211 Assignment 10 - Part 1
-- Music Artists Database Schema
--
-- Models music artists, the albums they create,
-- and the songs that appear on those albums.

-- Drop tables if they already exist (for clean re-runs)
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;

-- ── Artists ────────────────────────────────────────────────────────────────
-- We only care about the name of the artist
CREATE TABLE artist (
    id      INTEGER PRIMARY KEY,
    name    TEXT NOT NULL
);

-- ── Albums ─────────────────────────────────────────────────────────────────
-- Every album has a name and one associated artist
CREATE TABLE album (
    id          INTEGER PRIMARY KEY,
    name        TEXT    NOT NULL,
    artist_id   INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

-- ── Songs ──────────────────────────────────────────────────────────────────
-- Each song has a name, associated album, track number, and length in seconds
CREATE TABLE song (
    id              INTEGER PRIMARY KEY,
    name            TEXT    NOT NULL,
    album_id        INTEGER NOT NULL,
    track_number    INTEGER NOT NULL,
    length_seconds  INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album(id)
);
