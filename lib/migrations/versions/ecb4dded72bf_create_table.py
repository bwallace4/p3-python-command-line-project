"""create table

Revision ID: ecb4dded72bf
Revises: 
Create Date: 2023-08-27 10:39:23.849434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecb4dded72bf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
   op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=True),
        sa.Column('comment', sa.String(), nullable=True),
        sa.Column('movie_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
