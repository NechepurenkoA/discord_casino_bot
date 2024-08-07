"""movies and actors

Revision ID: a3be328380f2
Revises: 5efee8d2d739
Create Date: 2024-07-15 18:23:09.495514

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "a3be328380f2"
down_revision: Union[str, None] = "5efee8d2d739"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum(
        "HORROR",
        "ROMANCE",
        "ACTION",
        "THRILLER",
        "DOCUMENTARY",
        "DRAMA",
        "BIOGRAPHY",
        "HISTORY",
        name="genres",
    ).create(op.get_bind())
    sa.Enum("MALE", "FEMALE", name="genders").create(op.get_bind())
    op.create_table(
        "actors",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("second_name", sa.String(), nullable=False),
        sa.Column("third_name", sa.String(), nullable=False),
        sa.Column("birth_date", sa.Date(), nullable=False),
        sa.Column(
            "gender",
            postgresql.ENUM("MALE", "FEMALE", name="genders", create_type=False),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "movies",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column(
            "genre",
            postgresql.ARRAY(
                postgresql.ENUM(
                    "HORROR",
                    "ROMANCE",
                    "ACTION",
                    "THRILLER",
                    "DOCUMENTARY",
                    "DRAMA",
                    "BIOGRAPHY",
                    "HISTORY",
                    name="genres",
                    create_type=False,
                )
            ),
            nullable=False,
        ),
        sa.Column("date_published", sa.Date(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("movies")
    op.drop_table("actors")
    sa.Enum("MALE", "FEMALE", name="genders").drop(op.get_bind())
    sa.Enum(
        "HORROR",
        "ROMANCE",
        "ACTION",
        "THRILLER",
        "DOCUMENTARY",
        "DRAMA",
        "BIOGRAPHY",
        "HISTORY",
        name="genres",
    ).drop(op.get_bind())
    # ### end Alembic commands ###
