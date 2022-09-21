'''Implementation of acac: Arcade Classics Anniversary Collection'''
import logging
import lzma
import os
from gex.lib.tasks.basetask import BaseTask
from gex.lib.tasks import helpers
from gex.lib.utils.blob import transforms

logger = logging.getLogger('gextoolbox')

class ACACTask(BaseTask):
    '''Implements acac: Arcade Classics Anniversary Collection'''
    _task_name = "ags"
    _title = "Arcade Classics Anniversary Collection"
    _details_markdown = ''''''
    _default_input_folder = helpers.gen_steam_app_default_folder("Arcade Classics Anniversary Collection")
    _input_folder_desc = "Arcade Classics Anniversary Collection install folder"
    _short_description = ""

    _prop_info = {
        "include-partials": {
            "description": "Include the partial ROMs that are missing data; useful for mixing with other sources or investigation",
            "default": False,
            "type": "Boolean"
        }
    }

    _game_info_map = [
        {
            "name": "AJAX (J)",
            "filename": "ajaxj.zip",
            'status': 'good',
            "notes": [],
            "in": {
                "start": 0x11B610,
                "length": 3473920
            },
            "out": [
                {"filename": "770_l01.n11", "start": 0x000000, "length": 0x10000},
                {"filename": "770_l02.n12", "start": 0x020000, "length": 0x10000},
                {"filename": "770_l05.i16", "start": 0x030000, "length": 0x8000},
                {"filename": "770_f04.g16", "start": 0x038000, "length": 0x10000},
                {"filename": "770_f03.f16", "start": 0x048000, "length": 0x8000},
                {"filename": "770c13.n22", "start": 0x090000, "length": 0x40000},
                {"filename": "770c12.k22", "start": 0x0D0000, "length": 0x40000},
                {"filename": "770c09.n4", "start": 0x110000, "length": 0x80000},
                {"filename": "770c08.k4", "start": 0x190000, "length": 0x80000},
                {"filename": "770c06.f4", "start": 0x210000, "length": 0x40000},
                {"filename": "770c07.h4", "start": 0x250000, "length": 0x40000},
                {"filename": "770c10", "start": 0x290000, "length": 0x40000},
                {"filename": "770c11", "start": 0x2D0000, "length": 0x80000},
                {"filename": "63s241.j11", "start": 0x350000, "length": 0x200},
            ],
        },
        {
            "name": "AJAX",
            "filename": "ajax.zip",
            'status': 'no-rom',
            "notes": [2],
        },
        {
            "name": "Typhoon",
            "filename": "typhoon.zip",
            'status': 'good',
            "notes": [],
            "in": {
                "start": 0x11B610,
                "length": 3473920
            },
            "out": [
                {"filename": "770_k01.n11", "start": 0x050000, "length": 0x10000},
                {"filename": "770_k02.n12", "start": 0x060000, "length": 0x10000},
                {"filename": "770_k05.i16", "start": 0x070000, "length": 0x8000},
                {"filename": "770_f04.g16", "start": 0x038000, "length": 0x10000},
                {"filename": "770_h03.f16", "start": 0x088000, "length": 0x8000},
                {"filename": "770c13.n22", "start": 0x090000, "length": 0x40000},
                {"filename": "770c12.k22", "start": 0x0D0000, "length": 0x40000},
                {"filename": "770c09.n4", "start": 0x110000, "length": 0x80000},
                {"filename": "770c08.k4", "start": 0x190000, "length": 0x80000},
                {"filename": "770c06.f4", "start": 0x210000, "length": 0x40000},
                {"filename": "770c07.h4", "start": 0x250000, "length": 0x40000},
                {"filename": "770c10", "start": 0x290000, "length": 0x40000},
                {"filename": "770c11", "start": 0x2D0000, "length": 0x80000},
                {"filename": "63s241.j11", "start": 0x350000, "length": 0x200},
            ],
        },
        {
            "name": "Haunted Castle (Version M)",
            "filename": "hcastle.zip",
            'status': 'good',
            "notes": [],
            "in": {
                "start": 0x22E110,
                "length": 3310848
            },
            "out": [
                {"filename": "m03.k12", "start": 0x078000, "length": 0x8000},
                {"filename": "b06.k8", "start": 0x080000, "length": 0x20000},
                {"filename": "768e01.e4", "start": 0x0A0000, "length": 0x8000},
                {"filename": "768c07.e17", "start": 0x0A8000, "length": 0x80000},
                {"filename": "768c09.g21", "start": 0x128000, "length": 0x80000},
                {"filename": "768c08.g19", "start": 0x1A8000, "length": 0x80000},
                {"filename": "768c04.j5", "start": 0x228000, "length": 0x80000},
                {"filename": "768c05.j6", "start": 0x2A8000, "length": 0x80000},
                {"filename": "768c13.j21", "start": 0x328000, "length": 0x100},
                {"filename": "768c11.i4", "start": 0x328000, "length": 0x100},
                {"filename": "768c14.j22", "start": 0x328100, "length": 0x100},
                {"filename": "768c10.i3", "start": 0x328100, "length": 0x100},
                {"filename": "768b12.d20", "start": 0x328400, "length": 0x100},
            ],
        },
        {
            "name": "Haunted Castle (Version E)",
            "filename": "hcastlee.zip",
            'status': 'good',
            "notes": [],
            "in": {
                "start": 0x22E110,
                "length": 3310848
            },
            "out": [
                {"filename": "768e03.k12", "start": 0x028000, "length": 0x8000},
                {"filename": "768e06.k8", "start": 0x030000, "length": 0x20000},
                {"filename": "768e01.e4", "start": 0x0A0000, "length": 0x8000},
                {"filename": "768c07.e17", "start": 0x0A8000, "length": 0x80000},
                {"filename": "768c09.g21", "start": 0x128000, "length": 0x80000},
                {"filename": "768c08.g19", "start": 0x1A8000, "length": 0x80000},
                {"filename": "768c04.j5", "start": 0x228000, "length": 0x80000},
                {"filename": "768c05.j6", "start": 0x2A8000, "length": 0x80000},
                {"filename": "768c13.j21", "start": 0x328000, "length": 0x100},
                {"filename": "768c11.i4", "start": 0x328000, "length": 0x100},
                {"filename": "768c14.j22", "start": 0x328100, "length": 0x100},
                {"filename": "768c10.i3", "start": 0x328100, "length": 0x100},
                {"filename": "768b12.d20", "start": 0x328400, "length": 0x100},
            ],
        },
        {
            "name": "Haunted Castle (Version K)",
            "filename": "hcastlek.zip",
            'status': 'good',
            "notes": [],
            "in": {
                "start": 0x22E110,
                "length": 3310848
            },
            "out": [
                {"filename": "768k03.k12", "start": 0x050000, "length": 0x8000},
                {"filename": "768g06.k8", "start": 0x058000, "length": 0x20000},
                {"filename": "768e01.e4", "start": 0x0A0000, "length": 0x8000},
                {"filename": "768c07.e17", "start": 0x0A8000, "length": 0x80000},
                {"filename": "768c09.g21", "start": 0x128000, "length": 0x80000},
                {"filename": "768c08.g19", "start": 0x1A8000, "length": 0x80000},
                {"filename": "768c04.j5", "start": 0x228000, "length": 0x80000},
                {"filename": "768c05.j6", "start": 0x2A8000, "length": 0x80000},
                {"filename": "768c13.j21", "start": 0x328000, "length": 0x100},
                {"filename": "768c11.i4", "start": 0x328000, "length": 0x100},
                {"filename": "768c14.j22", "start": 0x328100, "length": 0x100},
                {"filename": "768c10.i3", "start": 0x328100, "length": 0x100},
                {"filename": "768b12.d20", "start": 0x328400, "length": 0x100},
            ],
        },
        {
            "name": "Akuma-Jou Dracula (Version N)",
            "filename": "akumajoun.zip",
            'status': 'good',
            "notes": [],
            "in": {
                "start": 0x22E110,
                "length": 3310848
            },
            "out": [
                {"filename": "768n03.k12", "start": 0x000000, "length": 0x8000},
                {"filename": "768j06.k8", "start": 0x008000, "length": 0x20000},
                {"filename": "768e01.e4", "start": 0x0A0000, "length": 0x8000},
                {"filename": "768c07.e17", "start": 0x0A8000, "length": 0x80000},
                {"filename": "768c09.g21", "start": 0x128000, "length": 0x80000},
                {"filename": "768c08.g19", "start": 0x1A8000, "length": 0x80000},
                {"filename": "768c04.j5", "start": 0x228000, "length": 0x80000},
                {"filename": "768c05.j6", "start": 0x2A8000, "length": 0x80000},
                {"filename": "768c13.j21", "start": 0x328000, "length": 0x100},
                {"filename": "768c11.i4", "start": 0x328000, "length": 0x100},
                {"filename": "768c14.j22", "start": 0x328100, "length": 0x100},
                {"filename": "768c10.i3", "start": 0x328100, "length": 0x100},
                {"filename": "768b12.d20", "start": 0x328400, "length": 0x100},
            ],
        },
        {
            "name": "nemesis",
            "filename": "nemesis.zip",
            'status': 'partial',
            "notes": [1],
            "in": {
                "start": 0x22E110,
                "length": 74752
            },
        },
        {
            "name": "salamand.zip",
            "filename": "salamand",
            'status': 'partial',
            "notes": [1],
            "in": {
                "start": 0x4165D0,
                "length": 4415040
            },
        },
        {
            "name": "scramble",
            "filename": "scramble.zip",
            'status': 'partial',
            "notes": [1]
        },
        {
            "name": "thunderx",
            "filename": "thunderx.zip",
            'status': 'partial',
            "notes": [1],
            "in": {
                "start": 0x4D13D0,
                "length": 1900800
            },
        },
        {
            "name": "twinbee",
            "filename": "twinbee.zip",
            'status': 'partial',
            "notes": [1],
            "in": {
                "start": 0x2F2DE0,
                "length": 541184
            },
        },
        {
            "name": "vulcan",
            "filename": "vulcan.zip",
            'status': 'partial',
            "notes": [1],
            "in": {
                "start": 0x37C280,
                "length": 3080192
            },
        }
    ]

    _out_file_notes = {
        "1": "This game is not yet extractable; it might not be implemented as a usable ROM.",
        "2": "This variant does not appear to be present in this collection."
    }

    def __init__(self):
        super().__init__()
        self._out_file_list = map(lambda x: {
            'filename': x['filename'],
            'game': f"{x['name']}",
            'system': "Arcade",
            "status": x['status'],
            "notes": x['notes']},
            self._game_info_map)

    def execute(self, in_dir, out_dir):
        src_file = os.path.join(in_dir, "AA_AC_ArcadeClassics.exe")
        with open(src_file, 'rb') as src_file:
            src_contents = src_file.read()

        for game in self._game_info_map:
            if game.get('status') == "no-rom":
                logger.info(f"Skipping {game['name']} as there is no ROM to extract...")
                continue

            is_partial = game.get('status') == "partial"
            if not self._props.get('include-partials') and is_partial:
                logger.info(f"Skipping {game['name']} as this tool cannot extract a working copy...")
                continue

            logger.info(f"Extracting {game['name']}...")
            zip_files = {}

            # Get the specified decompression section
            contents = transforms.cut(src_contents, game['in']['start'], length=game['in']['length'])

            lzd = lzma.LZMADecompressor()
            contents = lzd.decompress(contents)
            if is_partial:
                zip_files["decompressed_blob"] = contents

            for work_file in game.get('out') or []:
                zip_files[work_file['filename']] = transforms.cut(contents, work_file['start'], length=work_file['length'])

            filename = f"partial_{game['filename']}" if  is_partial else game['filename']
            logger.info(f"Saving {filename}...")
            with open(os.path.join(out_dir, filename), "wb") as out_file:
                out_file.write(helpers.build_zip(zip_files))

        logger.info("Processing complete.")
