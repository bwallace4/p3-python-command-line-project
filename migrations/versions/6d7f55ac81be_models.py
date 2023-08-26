"""models

Revision ID: 6d7f55ac81be
Revises: fe5ecc3ec14e
Create Date: 2023-08-25 21:42:58.640110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d7f55ac81be'
down_revision: Union[str, None] = 'fe5ecc3ec14e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   op.create_table('directors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('number_of_films', sa.Integer(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
   op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('movie_length', sa.Integer(), nullable=True),
    sa.Column('director_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['director_id'], ['directors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
   op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('id')
    # ### end Alembic commands ###
    )


def downgrade() -> None:
         # ### commands auto generated by Alembic - please adjust! ###
     op.drop_table('reviews')
     op.drop_table('movies')
     op.drop_table('directors')
         # ### end Alembic commands ###