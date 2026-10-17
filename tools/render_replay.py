"""Render a schematic GIF from a downloaded official Kaggriculture episode.

Requires Pillow. Does not run the agent, simulate actions, or alter recorded states.
Usage: python3 tools/render_replay.py INPUT.json[.gz] OUTPUT.gif
"""
import argparse
import gzip
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def font(size):
    for name in ['Arial.ttf', '/System/Library/Fonts/Supplemental/Arial.ttf',
                 '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def render(source, destination):
    raw = source.read_bytes()
    replay = json.loads(gzip.decompress(raw) if source.suffix == '.gz' else raw)
    steps = replay['steps']
    names = replay['info']['TeamNames']
    colors = ['#64748b', '#087f83']
    crop_colors = {'WHEAT': '#e9cc6d', 'STRAWBERRY': '#f3b3b4', 'MELON': '#b0d8ac',
                   'CARROT': '#f3bd83', 'TOMATO': '#e69189'}
    short = {'WHEAT': 'WH', 'STRAWBERRY': 'ST', 'MELON': 'ME', 'CARROT': 'CA',
             'TOMATO': 'TO', 'COW': 'CW', 'SHEEP': 'SH', 'CHICKEN': 'CH', 'GOOSE': 'GO'}
    cash = [[float(step[0]['observation']['farms'][seat]['money']) for step in steps]
            for seat in range(2)]
    ymax = max(max(row) for row in cash) * 1.05
    indices = list(range(0, len(steps), 12))
    if indices[-1] != len(steps) - 1:
        indices.append(len(steps) - 1)
    frames = []
    for index in indices:
        obs = steps[index][0]['observation']
        im = Image.new('RGB', (1040, 800), '#f5f7fa')
        d = ImageDraw.Draw(im)
        d.text((34, 22), 'Kaggriculture | Official match replay', font=font(27), fill='#142c42')
        d.text((34, 58), f"Episode {replay['info']['EpisodeId']}  |  Recorded state {index + 1}/{len(steps)}  |  Day {obs['day'] + 1}",
               font=font(17), fill='#536579')
        for seat, x in enumerate([44, 564]):
            farm = obs['farms'][seat]
            d.text((x, 100), names[seat], font=font(22), fill=colors[seat])
            d.text((x, 131), f"Bank: {farm['money']:,.0f} coins  |  Workers: {1 + len(farm['hands'])}",
                   font=font(17), fill='#263d50')
            for y, row in enumerate(farm['tiles']):
                for xx, tile in enumerate(row):
                    label = ''
                    color = '#eee9db'
                    if tile == 'LOCKED':
                        color = '#cbd2dc'
                    elif isinstance(tile, dict):
                        kind = tile.get('kind')
                        if kind == 'PLANT':
                            label = short.get(tile['crop'], tile['crop'][:2])
                            color = crop_colors.get(tile['crop'], '#b0d8ac')
                        elif kind in ['COOP', 'PASTURE', 'ANIMAL']:
                            animal = tile.get('animal', tile.get('species', ''))
                            label = short.get(animal, animal[:2]) or ('CO' if kind == 'COOP' else 'PA')
                            color = '#d8c8e9'
                        elif kind == 'WEED':
                            label = '~'
                            color = '#91a589'
                    bx, by = x + xx * 40, 168 + y * 40
                    d.rectangle((bx, by, bx + 38, by + 38), fill=color)
                    if label:
                        d.text((bx + 4, by + 6), label, font=font(13), fill='#33413f')
            for actor, pos in enumerate([farm['farmer'], *farm['hands']]):
                bx, by = x + pos[0] * 40 + 27, 168 + pos[1] * 40 + 27
                d.ellipse((bx - 9, by - 9, bx + 9, by + 9), fill='#bb4b30' if actor == 0 else '#263d50')
                d.text((bx, by), 'F' if actor == 0 else 'H', anchor='mm', font=font(10), fill='white')
        d.text((44, 580), 'WH wheat   ST strawberry   ME melon   CA carrot   TO tomato', font=font(13), fill='#536579')
        d.text((44, 600), 'CO coop   PA pasture   CW cow   SH sheep   CH chicken   GO goose   F farmer   H hand   Gray locked', font=font(13), fill='#536579')
        left, top, width, height = 110, 641, 880, 94
        d.text((44, top), 'Bank', font=font(14), fill='#536579')
        d.text((44, top + 20), f'{ymax / 1000:.0f}k', font=font(12), fill='#536579')
        d.line((left, top, left, top + height, left + width, top + height), fill='#a9b6c3', width=1)
        for seat in range(2):
            points = [(left + j * width / (len(steps) - 1), top + height - cash[seat][j] / ymax * height)
                      for j in range(index + 1)]
            if len(points) > 1:
                d.line(points, fill=colors[seat], width=3)
        d.text((left, top + height + 3), 'Season start', font=font(12), fill='#536579')
        d.text((left + width - 85, top + height + 3), 'Season end', font=font(12), fill='#536579')
        footer = 'Recorded states sampled every 12 turns | Schematic data visualization, not the official renderer'
        if index == len(steps) - 1:
            footer = f"Final: We Forgot To Water {replay['rewards'][1]:,.0f} - {replay['rewards'][0]:,.0f} Peihao Chen Caesar | Win"
        d.text((34, 775), footer, font=font(13), fill='#142c42')
        frames.append(im)
    destination.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(destination, save_all=True, append_images=frames[1:],
                   duration=[240] * (len(frames) - 1) + [2400], loop=0, optimize=True)
    print(f'Rendered {len(frames)} frames from {len(steps)} official recorded states: {destination}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('destination', type=Path)
    args = parser.parse_args()
    render(args.source, args.destination)
