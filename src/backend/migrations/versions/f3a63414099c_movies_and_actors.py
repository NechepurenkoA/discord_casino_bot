"""movies and actors

Revision ID: f3a63414099c
Revises: 5efee8d2d739
Create Date: 2024-07-14 23:54:35.355543

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "f3a63414099c"
down_revision: Union[str, None] = "5efee8d2d739"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum(
        "HORROR", "ROMANCE", "ACTION", "THRILLER", "DOCUMENTARY", name="genre"
    ).create(op.get_bind())
    op.create_table(
        "actors",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("second_name", sa.String(), nullable=False),
        sa.Column("third_name", sa.String(), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "movies",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column(
            "genre",
            postgresql.ENUM(
                "HORROR",
                "ROMANCE",
                "ACTION",
                "THRILLER",
                "DOCUMENTARY",
                name="genre",
                create_type=False,
            ),
            nullable=False,
        ),
        sa.Column("date_published", sa.Date(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "movies_actors",
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("actor_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["actor_id"],
            ["actors.id"],
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movies.id"],
        ),
        sa.PrimaryKeyConstraint("movie_id", "actor_id", "id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("movies_actors")
    op.drop_table("movies")
    op.drop_table("actors")
    sa.Enum(
        "HORROR", "ROMANCE", "ACTION", "THRILLER", "DOCUMENTARY", name="genre"
    ).drop(op.get_bind())
    # ### end Alembic commands ###
