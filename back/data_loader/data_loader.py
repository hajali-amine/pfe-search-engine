from graph_query_builder.directions_enum import Direction
from graph_query_builder.query_builder import QueryBuilder


class DataLoader:
    @staticmethod
    def load(neo, data):
        query_builder = QueryBuilder()
        query_builder.merge().node("l", "Location", name=data["location"]).merge().node(
            "c", "Company", name=data["company"], logo=data["logo"]
        ).merge().node(
            "i",
            "Internship",
            name=data["title"],
            desc=data["description"],
            link=data["link"],
        ).merge().node(
            "i", ""
        ).relation(
            "in", "IN", Direction.NONE
        ).node(
            "l", ""
        ).merge().node(
            "i", ""
        ).relation(
            "at", "AT", Direction.NONE
        ).node(
            "c", ""
        )

        for index, skillset in enumerate(data["skills"]):
            ((skill, theme),) = skillset.items()
            query_builder.merge().node(f"s{index}", "Skill", name=skill).merge().node(
                f"t{index}", "Theme", name=theme
            ).merge().node(f"s{index}", "").relation(
                f"fits{index}", "FITS", Direction.NONE
            ).node(
                f"t{index}", ""
            ).merge().node(
                f"s{index}", ""
            ).relation(
                f"require{index}", "REQUIRE", Direction.NONE
            ).node(
                "i", ""
            )

        neo.execute_query(query_builder.build())
