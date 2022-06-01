from graph_query_builder.directions_enum import Direction
from graph_query_builder.query_builder import QueryBuilder


class DataReader:    
    @staticmethod
    def search_by_filter(neo, filter, search):
        query_builder = QueryBuilder()
        query_builder\
            .match().node("l", "Location").relation("in", "IN", Direction.NONE).node("i", "Internship")\
                .match().node("c", "Company").relation("at", "AT", Direction.NONE).node("i", "Internship")\
                    .match().node("i", "Internship").relation("req", "REQUIRE", Direction.NONE).node("s", "Skill")\
                        .where(f"toLower({filter[0]}.name) CONTAINS toLower('{search}')")\
                            .to_return("{internship: i.name, description:i.description, location: l.name, company: c.name, logo: c.logo, skills: COLLECT(s.name)}")
        return neo.execute_query(query_builder.build())

    @staticmethod
    def search_by_skill(neo, search):
        query_builder = QueryBuilder()

        query_builder\
            .match().node("i", "Internship").relation("req", "REQUIRE", Direction.NONE).node("s", "Skill")\
                .match().node("l", "Location").relation("in", "IN", Direction.NONE).node("i", "Internship")\
                    .match().node("c", "Company").relation("at", "AT", Direction.NONE).node("i", "Internship")\
                        .match().node("s_prime", "Skill").relation("req_prime", "REQUIRE", Direction.NONE).node("i", "Internship")\
                            .where(f"toLower(s.name) CONTAINS toLower('{search}')")\
                                .to_return("{internship: i.name, description:i.description, link:i.link, location: l.name, company: c.name, logo: c.logo, skills: COLLECT(s_prime.name)}")
        main_result = neo.execute_query(query_builder.build())
        print(main_result)

        query_builder\
            .match().node("t", "Theme").relation("fits", "FITS", Direction.NONE).node("s", "Skill")\
                .match().node("related_skills", "Skill").relation("related_fits", "FITS", Direction.NONE).node("t", "Theme")\
                    .match().node("i", "Internship").relation("req", "REQUIRE", Direction.NONE).node("related_skills", "Skill")\
                        .match().node("l", "Location").relation("in", "IN", Direction.NONE).node("i", "Internship")\
                            .match().node("c", "Company").relation("at", "AT", Direction.NONE).node("i", "Internship")\
                                .match().node("s_prime", "Skill").relation("req_prime", "REQUIRE", Direction.NONE).node("i", "Internship")\
                                    .where(f"toLower(s.name) CONTAINS toLower('{search}')")\
                                        .to_return("{internship: i.name, description:i.description, link:i.link, location: l.name, company: c.name, logo: c.logo, skills: COLLECT(s_prime.name)}")
        related_results = neo.execute_query(query_builder.build())
        print(related_results)

        difference = []
        for internship in related_results:
            if internship not in main_result:
                difference.append(internship)
        
        main_result.extend(difference)
        print(main_result)

        return main_result

