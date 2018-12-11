import xmltodict


def parse(file_path):
    with open(file_path) as fd:
        doc = xmltodict.parse(fd.read())
        rows = doc["Level"]["Rows"]
        parsed_bricks = []
        for row in rows["Row"]:
            row_number = int(row["@id"])
            blocks = row["Bricks"]
            for block in blocks["Brick"]:
                column_number = int(block["@column"])
                color_id = int(block.get("@color", 0))
                block_type = int(block.get("@type", 0))
                parsed_bricks.append((row_number, column_number, color_id, block_type))
        return parsed_bricks
